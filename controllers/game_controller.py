import pygame
from assets.config import LARGURA, ALTURA, CORES, get_fonts
from assets.strings import textos
from assets.questions import perguntas
from views.tela_inicio import desenhar_tela_inicio
from views.tela_ranking import desenhar_tela_ranking
from views.tela_resultado import desenhar_tela_resultado  
from controllers.player_controller import criar_jogador, atualizar_nome
from views.tela_jogo import desenhar_tela_jogo
from models.forca_game import ForcaGame

def iniciar_jogo():
    pygame.init()
    screen = pygame.display.set_mode((LARGURA, ALTURA))
    clock = pygame.time.Clock()
    fontes = get_fonts()

    # Imagens
    img_trofeu = pygame.image.load("assets/img/trofeu.png").convert_alpha()
    img_sair = pygame.image.load("assets/img/sair.png").convert_alpha()
    img_idade = pygame.image.load("assets/img/idade.png").convert_alpha()
    img_python = pygame.image.load("assets/img/python.png").convert_alpha()
    img_voltar = pygame.image.load("assets/img/voltar.png").convert_alpha()
    img_jogador = pygame.image.load("assets/img/jogador.png").convert_alpha()
    img_pontos = pygame.image.load("assets/img/pontos.png").convert_alpha()
    img_relogio = pygame.image.load("assets/img/relogio.png").convert_alpha()
    img_vidas = pygame.image.load("assets/img/vidas.png").convert_alpha()

    input_ativo = False
    caixa_texto = pygame.Rect(LARGURA // 2 - 260, ALTURA // 2 - 50, 546, 68)
    jogador = criar_jogador()
    forca_game = ForcaGame(perguntas)

    estado = "inicio"
    running = True

    # Para armazenar os botões da tela de resultado
    btn_reiniciar_rect = btn_sair_rect = None
    botao_inicio_rect = botao_creditos_rect = botao_sair_rect = None
    botao_voltar_rect = img_voltar_rect = None
    ultimo_tick = pygame.time.get_ticks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if estado == "inicio":
                if event.type == pygame.KEYDOWN and input_ativo:
                    if event.key == pygame.K_RETURN:
                        jogador.nome = jogador.nome.strip()
                        if jogador.nome:
                            forca_game.iniciar(jogador.nome)
                            print(f"Nome do jogador: {jogador.nome}")
                    else:
                        atualizar_nome(jogador, event)
                        print(f"Nome do jogador: {jogador.nome}")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if caixa_texto.collidepoint(event.pos):
                        input_ativo = True
                    else:
                        input_ativo = False

                    if botao_inicio_rect and botao_inicio_rect.collidepoint(event.pos):
                        print("Clicou no botão COMEÇAR")
                        if jogador.nome.strip():
                            forca_game.iniciar(jogador.nome)
                            estado = "jogo"
                    elif botao_creditos_rect and botao_creditos_rect.collidepoint(event.pos):
                        print("Clicou no botão RANKING")
                        estado = "ranking"
                    elif botao_sair_rect and botao_sair_rect.collidepoint(event.pos):
                        print("Clicou no botão SAIR")
                        running = False

            elif estado == "ranking":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_voltar_rect and botao_voltar_rect.collidepoint(event.pos):
                        estado = "inicio"

            elif estado == "jogo":
                agora = pygame.time.get_ticks()
                if agora - ultimo_tick >= 1000:
                    ultimo_tick = agora
                    # Só atualiza o tempo se ainda tem vidas
                    if forca_game.jogador.vidas > 0:
                        forca_game.atualizar_tempo()
                    else:
                        estado = "resultado"
                        continue

                img_voltar_rect = desenhar_tela_jogo(
                    screen, fontes, textos, CORES,
                    forca_game,
                    img_jogador, img_pontos, img_relogio, img_vidas, img_voltar
                )
                mouse_pos = pygame.mouse.get_pos()
                if img_voltar_rect and img_voltar_rect.collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

                # AVANÇA PARA A PRÓXIMA QUESTÃO SE NECESSÁRIO
                if forca_game.avancar_proxima:
                    pygame.time.delay(1000)  # Pequena pausa para feedback visual
                    forca_game.proxima_pergunta()
                    forca_game.avancar_proxima = False

                 # Verifica se jogo terminou
                if forca_game.jogador.vidas == 0 or forca_game.pergunta_atual >= len(perguntas):
                    estado = "resultado"
                    continue

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if img_voltar_rect and img_voltar_rect.collidepoint(event.pos):
                        estado = "inicio"
                        continue

                 # --- DETECTA CLIQUE NAS LETRAS ---
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # Repita a lógica de posição dos botões das letras
                    alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
                    letras_por_linha = 10
                    espacamento = 50
                    largura_botao = 40
                    altura_botao = 40
                    x_alfabeto_inicial = LARGURA - 720
                    margem_top = 210 + 150 + 40 + 60 # y_ret + altura_ret + 40 + 60
                    for i, letra in enumerate(alfabeto):
                        linha = i // letras_por_linha
                        coluna = i % letras_por_linha
                        x = x_alfabeto_inicial + coluna * espacamento
                        y = margem_top + linha * (altura_botao + 15)
                        rect = pygame.Rect(x, y, largura_botao, altura_botao)
                        if rect.collidepoint(mouse_x, mouse_y):
                            # Só processa se a letra ainda não foi tentada
                            if letra not in forca_game.jogador.letras_adivinhadas:
                                forca_game.verificar_letra(letra)
                                 # Se errou, o model já atualiza vidas e erros
                                # Se acertou, só adiciona a letra
                            break

                if forca_game.avancar_proxima:
                    pygame.time.delay(1000)
                    forca_game.proxima_pergunta()
                    forca_game.avancar_proxima = False

            elif estado == "resultado":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn_reiniciar_rect and btn_reiniciar_rect.collidepoint(event.pos):
                        # Reiniciar o jogo
                        forca_game = ForcaGame(perguntas)
                        jogador.vidas = 6
                        jogador.letras_adivinhadas.clear()
                        jogador.pontuacao = 0
                        forca_game.iniciar(jogador.nome)
                        estado = "jogo"
                    elif btn_sair_rect and btn_sair_rect.collidepoint(event.pos):
                        running = False

                img_voltar_rect = desenhar_tela_jogo(
                    screen, fontes, textos, CORES,
                    forca_game,
                    img_jogador, img_pontos, img_relogio, img_vidas, img_voltar
                )
                mouse_pos = pygame.mouse.get_pos()
                if img_voltar_rect and img_voltar_rect.collidepoint(mouse_pos):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else:
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        # --- DESENHO DAS TELAS ---
        if estado == "inicio":
            botao_inicio_rect, botao_creditos_rect, botao_sair_rect = desenhar_tela_inicio(
                screen, fontes, textos, CORES,
                input_ativo, caixa_texto, jogador.nome,
                img_trofeu, img_sair, img_idade, img_python
            )
            mouse_pos = pygame.mouse.get_pos()
            if (botao_inicio_rect and botao_inicio_rect.collidepoint(mouse_pos)) or \
               (botao_creditos_rect and botao_creditos_rect.collidepoint(mouse_pos)) or \
               (botao_sair_rect and botao_sair_rect.collidepoint(mouse_pos)):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            elif caixa_texto.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        elif estado == "ranking":
            botao_voltar_rect = desenhar_tela_ranking(screen, fontes, textos, CORES, img_voltar)
            mouse_pos = pygame.mouse.get_pos()
            if botao_voltar_rect and botao_voltar_rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        elif estado == "jogo":
            img_voltar_rect = desenhar_tela_jogo(
                screen, fontes, textos, CORES,
                forca_game,
                img_jogador, img_pontos, img_relogio, img_vidas, img_voltar
            )


        elif estado == "resultado":
            btn_reiniciar_rect, btn_sair_rect = desenhar_tela_resultado(
                screen, fontes, textos, CORES,
                None, None,
                forca_game.jogador.pontuacao,
                perguntas
            )

            mouse_pos = pygame.mouse.get_pos()
            if img_voltar_rect and img_voltar_rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
