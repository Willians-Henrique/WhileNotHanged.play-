import pygame

def desenhar_botao(tela, rect, cor_fundo, cor_borda, texto, fonte, cor_texto, border_radius=20):
    pygame.draw.rect(tela, cor_fundo, rect, 0, border_radius=border_radius)
    pygame.draw.rect(tela, cor_borda, rect, 3, border_radius=border_radius)
    tela.blit(
        texto,
        (rect.x + rect.width//2 - texto.get_width()//2, rect.y + rect.height//2 - texto.get_height()//2)
    )

def desenhar_forca(tela, erros, cores, forca_x=100, forca_y=150):
    PRETO = cores["PRETO"]
    PELE = cores["pele"]
    
    # Estrutura da forca preta (usando os tamanhos e posições que você pediu)
    base_largura = 200
    base_altura = 20
    poste_altura = 400
    braco_largura = 150
    corda_altura = 50
    corda_largura = 20

    base_x = forca_x
    base_y = forca_y + 470  # ALTURA // 2 + 220, mas relativo ao forca_y

    pygame.draw.rect(tela, PRETO, (base_x, base_y, base_largura, base_altura))
    poste_x = base_x + base_largura // 2 - 10
    poste_y = base_y - poste_altura
    poste_largura = 20
    pygame.draw.rect(tela, PRETO, (poste_x, poste_y, poste_largura, poste_altura))
    braco_x = poste_x + poste_largura
    braco_y = poste_y
    braco_altura = 20
    pygame.draw.rect(tela, PRETO, (braco_x, braco_y, braco_largura, braco_altura))
    corda_x = braco_x + braco_largura
    corda_y_inicial = braco_y
    pygame.draw.rect(tela, PRETO, (corda_x, corda_y_inicial, corda_largura, corda_altura))

    # Boneco (apenas se houver erros)
    partes = [
        lambda: pygame.draw.circle(tela, PELE, (corda_x + corda_largura // 2, corda_y_inicial + corda_altura + 25), 25),  # cabeça
        lambda: pygame.draw.line(tela, PELE, (corda_x + corda_largura // 2, corda_y_inicial + corda_altura + 50), (corda_x + corda_largura // 2, corda_y_inicial + corda_altura + 150), 5),  # tronco
        lambda: pygame.draw.line(tela, PELE, (corda_x + corda_largura // 2, corda_y_inicial + corda_altura + 70), (corda_x + corda_largura // 2 - 35, corda_y_inicial + corda_altura + 100), 5),  # braço esq
        lambda: pygame.draw.line(tela, PELE, (corda_x + corda_largura // 2, corda_y_inicial + corda_altura + 70), (corda_x + corda_largura // 2 + 35, corda_y_inicial + corda_altura + 100), 5),  # braço dir
        lambda: pygame.draw.line(tela, PELE, (corda_x + corda_largura // 2, corda_y_inicial + corda_altura + 150), (corda_x + corda_largura // 2 - 25, corda_y_inicial + corda_altura + 200), 5),  # perna esq
        lambda: pygame.draw.line(tela, PELE, (corda_x + corda_largura // 2, corda_y_inicial + corda_altura + 150), (corda_x + corda_largura // 2 + 25, corda_y_inicial + corda_altura + 200), 5),  # perna dir
    ]
    for i in range(min(erros, len(partes))):
        partes[i]()