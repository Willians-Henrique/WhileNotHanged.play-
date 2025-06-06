import pygame
from assets.config import LARGURA, ALTURA, CORES, get_fonts
from assets.strings import textos
from assets.questions import perguntas
from views.tela_inicio import desenhar_tela_inicio
from views.tela_ranking import desenhar_tela_ranking
from controllers.player_controller import criar_jogador, atualizar_nome
from views.tela_jogo import desenhar_tela_jogo

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

    estado = "inicio"
    running = True

    # Variáveis do jogo
    tempo_restante = 120
    pergunta_atual = 0
    letras_adivinhadas = []
    letras_disponiveis = [chr(i) for i in range(65, 91)]
    erros_consecutivos = 0
    feedback = ""

    botao_inicio_rect = botao_creditos_rect = botao_sair_rect = None
    botao_voltar_rect = img_voltar_rect = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if estado == "inicio":
                if event.type == pygame.KEYDOWN and input_ativo:
                    if event.key == pygame.K_RETURN:
                        jogador.nome = jogador.nome.strip()
                        if jogador.nome:
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if img_voltar_rect and img_voltar_rect.collidepoint(event.pos):
                        estado = "inicio"
                # Aqui você pode adicionar lógica para clicar nas letras, etc.

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
                jogador.nome, jogador.vidas, jogador.pontuacao, tempo_restante,
                pergunta_atual, perguntas, letras_adivinhadas, letras_disponiveis,
                erros_consecutivos, feedback,
                img_jogador, img_pontos, img_relogio, img_vidas, img_voltar
            )
            mouse_pos = pygame.mouse.get_pos()
            if img_voltar_rect and img_voltar_rect.collidepoint(mouse_pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
