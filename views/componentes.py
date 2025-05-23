import pygame

def desenhar_botao(tela, rect, cor_fundo, cor_borda, texto, fonte, cor_texto, border_radius=20):
    pygame.draw.rect(tela, cor_fundo, rect, 0, border_radius=border_radius)
    pygame.draw.rect(tela, cor_borda, rect, 3, border_radius=border_radius)
    tela.blit(
        texto,
        (rect.x + rect.width//2 - texto.get_width()//2, rect.y + rect.height//2 - texto.get_height()//2)
    )