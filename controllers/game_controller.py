import pygame
from assets.config import LARGURA, ALTURA, CORES, get_fonts
from assets.strings import textos
from assets.questions import perguntas
from views.tela_inicio import desenhar_tela_inicio
from controllers.player_controller import criar_jogador, atualizar_nome
from views.tela_jogo import desenhar_tela_jogo

def iniciar_jogo():
    pygame.init()
    screen = pygame.display.set_mode((LARGURA, ALTURA))
    clock = pygame.time.Clock()
    fontes = get_fonts()

    img_trofeu = pygame.image.load("assets/img/trofeu.png").convert_alpha()
    img_sair = pygame.image.load("assets/img/sair.png").convert_alpha()
    img_idade = pygame.image.load("assets/img/idade.png").convert_alpha()
    img_python = pygame.image.load("assets/img/python.png").convert_alpha()

    input_ativo = False
    caixa_texto = pygame.Rect(LARGURA // 2 - 260, ALTURA // 2 - 50, 546, 68)
    jogador = criar_jogador()

    tempo_restante = 120
    pergunta_atual = 0
    letras_adivinhadas = []
    letras_disponiveis = [chr(i) for i in range(65, 91)]
    erros_consecutivos = 0
    feedback = ""

    # Controle de estado
    ESTADO_INICIO = "inicio"
    ESTADO_JOGO = "jogo"
    estado = ESTADO_INICIO

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if estado == ESTADO_INICIO:
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

                    botao_inicio_rect, botao_creditos_rect, botao_sair_rect = desenhar_tela_inicio(
                        screen, fontes, textos, CORES,
                        input_ativo, caixa_texto, jogador.nome, img_trofeu, img_sair,
                        img_idade, img_python
                    )

                    if botao_inicio_rect.collidepoint(event.pos):
                        print("Clicou no botão COMEÇAR")
                        estado = ESTADO_JOGO  # MUDA O ESTADO!
                        # (Se quiser, resete variáveis do jogo aqui)
                    if botao_creditos_rect.collidepoint(event.pos):
                        print("Clicou no botão CRÉDITOS")
                    if botao_sair_rect.collidepoint(event.pos):
                        print("Clicou no botão SAIR")
                        running = False

            elif estado == ESTADO_JOGO:
                # Aqui você pode tratar eventos do jogo (clique nas letras, etc)
                pass

        # --- DESENHO DAS TELAS ---
        if estado == ESTADO_INICIO:
            botao_inicio_rect, botao_creditos_rect, botao_sair_rect = desenhar_tela_inicio(
                screen, fontes, textos, CORES,
                input_ativo, caixa_texto, jogador.nome, img_trofeu, img_sair,
                img_idade, img_python
            )
        elif estado == ESTADO_JOGO:
            desenhar_tela_jogo(
                screen, fontes, textos, CORES,
                jogador.nome, jogador.vidas, jogador.pontuacao, tempo_restante,
                pergunta_atual, perguntas, letras_adivinhadas, letras_disponiveis,
                erros_consecutivos, feedback
            )

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

def loop_principal():
    """Loop principal do jogo: processa eventos, atualiza estado, desenha telas."""
    pass

def mudar_estado(novo_estado):
    """Altera o estado do jogo (tela início, jogo, resultado, créditos)."""
    pass

def atualizar_tempo():
    """Atualiza o timer do jogo e verifica se o tempo acabou."""
    pass

def encerrar_jogo():
    """Finaliza o pygame e encerra o programa."""
    pass