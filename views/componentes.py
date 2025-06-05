import pygame

def desenhar_botao(tela, rect, cor_fundo, cor_borda, texto, fonte, cor_texto, border_radius=20):
    pygame.draw.rect(tela, cor_fundo, rect, 0, border_radius=border_radius)
    pygame.draw.rect(tela, cor_borda, rect, 3, border_radius=border_radius)
    tela.blit(
        texto,
        (rect.x + rect.width//2 - texto.get_width()//2, rect.y + rect.height//2 - texto.get_height()//2)
    )

def desenhar_forca(tela, erros, cores, forca_x=100, forca_y=150):
    partes = [
        lambda: pygame.draw.rect(tela, cores["marrom"], (forca_x-20, forca_y+300, 300, 30)),
        lambda: pygame.draw.rect(tela, cores["marrom"], (forca_x+120, forca_y+50, 20, 250)),
        lambda: pygame.draw.rect(tela, cores["marrom"], (forca_x+120, forca_y+50, 150, 20)),
        lambda: pygame.draw.rect(tela, cores["marrom"], (forca_x+260, forca_y+50, 10, 50)),
        lambda: [
            pygame.draw.circle(tela, cores["pele"], (forca_x+265, forca_y+125), 25),
            pygame.draw.circle(tela, cores["preto"], (forca_x+255, forca_y+120), 3),
            pygame.draw.circle(tela, cores["preto"], (forca_x+275, forca_y+120), 3),
            pygame.draw.line(tela, cores["preto"], (forca_x+255, forca_y+140), (forca_x+275, forca_y+140), 2)
        ],
        lambda: pygame.draw.line(tela, cores["pele"], (forca_x+265, forca_y+150), (forca_x+265, forca_y+250), 5),
        lambda: pygame.draw.line(tela, cores["pele"], (forca_x+265, forca_y+170), (forca_x+230, forca_y+200), 5),
        lambda: pygame.draw.line(tela, cores["pele"], (forca_x+265, forca_y+170), (forca_x+300, forca_y+200), 5),
        lambda: pygame.draw.line(tela, cores["pele"], (forca_x+265, forca_y+250), (forca_x+240, forca_y+300), 5),
        lambda: pygame.draw.line(tela, cores["pele"], (forca_x+265, forca_y+250), (forca_x+290, forca_y+300), 5)
    ]
    # Desenha a estrutura da forca
    for i in range(4):
        partes[i]()
    # Desenha o boneco conforme os erros
    for i in range(4, 4 + min(erros, 6)):
        parte = partes[i]
        resultado = parte()
        if isinstance(resultado, list):
            for elemento in resultado:
                if callable(elemento):
                    elemento()