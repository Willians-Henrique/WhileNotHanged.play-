import pygame
from assets.config import LARGURA, ALTURA, CORES, get_fonts
from assets.strings import textos
from views.tela_inicio import desenhar_tela_inicio
from controllers.player_controller import criar_jogador, atualizar_nome

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

    running = True
    while running:
          # Desenha a tela e pega os retângulos dos botões
        botao_inicio_rect, botao_creditos_rect, botao_sair_rect = desenhar_tela_inicio(
            screen, fontes, textos, CORES,
            input_ativo, caixa_texto, jogador.nome
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if caixa_texto.collidepoint(event.pos):
                    input_ativo = True
                else:
                    input_ativo = False

                     # Verifica clique nos botões
                if botao_inicio_rect.collidepoint(event.pos):
                    print("Clicou no botão COMEÇAR")
                    # Aqui você pode avançar para o jogo
                if botao_creditos_rect.collidepoint(event.pos):
                    print("Clicou no botão CRÉDITOS")
                    # Aqui você pode mostrar os créditos
                if botao_sair_rect.collidepoint(event.pos):
                    print("Clicou no botão SAIR")
                   running = False

            if event.type == pygame.KEYDOWN and input_ativo:
                if event.key == pygame.K_RETURN:
                    jogador.nome = jogador.nome.strip()
                    if jogador.nome:
                        print(f"Nome do jogador: {jogador.nome}")
                        # Aqui você pode avançar para o jogo    
                else:
                    atualizar_nome(jogador, event)
                    print(f"Nome do jogador: {jogador.nome}")

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