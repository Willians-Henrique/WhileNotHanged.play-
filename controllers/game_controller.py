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

    input_ativo = False
    caixa_texto = pygame.Rect(LARGURA//2 - 200, ALTURA//2 + 50, 400, 60)
    jogador = criar_jogador()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if caixa_texto.collidepoint(event.pos):
                    input_ativo = True
                else:
                    input_ativo = False

            if event.type == pygame.KEYDOWN and input_ativo:
                if event.key == pygame.K_RETURN:
                    jogador.nome = jogador.nome.strip()
                    if jogador.nome:
                        print(f"Nome do jogador: {jogador.nome}")
                        # Aqui você pode avançar para o jogo    
                else:
                    atualizar_nome(jogador, event)
                    print(f"Nome do jogador: {jogador.nome}")

        desenhar_tela_inicio(
            screen, fontes, textos, CORES,
            input_ativo, caixa_texto, jogador.nome
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