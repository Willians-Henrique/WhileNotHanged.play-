import pygame
from assets.config import LARGURA, ALTURA, CORES, get_fonts
from assets.strings import textos
from views.tela_inicio import desenhar_tela_inicio

pygame.init()
screen = pygame.display.set_mode((LARGURA, ALTURA))
clock = pygame.time.Clock()
fontes = get_fonts()

# Estado mínimo para a tela de início
input_ativo = False
nome_jogador = ""
caixa_texto = pygame.Rect(LARGURA//2 - 200, ALTURA//2 + 50, 400, 60)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    desenhar_tela_inicio(
        screen, fontes, textos, CORES,
        input_ativo, caixa_texto, nome_jogador
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()