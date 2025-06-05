import pygame
from views.componentes import desenhar_botao


def desenhar_tela_inicio(
    tela, fontes, textos, cores, 
    input_ativo, caixa_texto, nome_jogador, img_trofeu,
    img_sair, img_idade, img_python
):
    #Desempacota as fontes e cores
    fonte_pequena = fontes["pequena"]
    fonte_media = fontes["media"]
    fonte_grande = fontes["grande"]
    fonte_titulo = fontes["titulo"]

    AMARELO = cores["AMARELO"]
    AMARELO_HOVER = cores["AMARELO_HOVER"]
    PRETO = cores["PRETO"]
    AZUL = cores["AZUL"]

    LARGURA, ALTURA = tela.get_size()

    #Fundo azul
    tela.fill(AZUL)
    s = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
    pygame.draw.rect(s, (173, 216, 230, 150), (0, 0, LARGURA, ALTURA))
    tela.blit(s, (0, 0))

    #Título 
    titulo = fonte_titulo.render(textos["titulo"], True, PRETO)

    #Retangulo amarelo
    titulo_rect = pygame.draw.rect(
        tela, AMARELO, 
        (LARGURA//2 - titulo.get_width()//2 - 20, 80, 
         titulo.get_width() + 40, titulo.get_height() + 40), 
        border_radius=20
    )
    #Escrevendo o titulo
    tela.blit(titulo, (LARGURA//2 - titulo.get_width()//2, 100))

    #Imagem do python no canto do retangulo amarelo
    img_python_rect = img_python.get_rect()
    img_python_rect.topright = (titulo_rect.right + 70, titulo_rect.top - 70)

    tela.blit(img_python, img_python_rect)

    #Retangulo do input
    pygame.draw.rect(
        tela, AMARELO_HOVER if input_ativo else AMARELO, 
        caixa_texto, 0, border_radius=15
    )
    pygame.draw.rect(tela, PRETO, caixa_texto, 3, border_radius=15)

    texto_nome = fonte_media.render(textos["digite_nome"], True, PRETO)
    tela.blit(texto_nome, (caixa_texto.x, caixa_texto.y - 40))

    texto_input = fonte_media.render(nome_jogador, True, PRETO)
    tela.blit(texto_input, (caixa_texto.x + 20, caixa_texto.y + 15))
    #Botão jogar
    texto_botao = fonte_grande.render(textos["comecar"], True, PRETO)
    largura_botao = max(288, texto_botao.get_width() + 60)
    botao_inicio_rect = pygame.Rect(
        LARGURA//2 - largura_botao//2, ALTURA//2 + 70, largura_botao, 70
    )
    mouse_pos = pygame.mouse.get_pos() #hover
    cor_botao = AMARELO_HOVER if botao_inicio_rect.collidepoint(mouse_pos) else AMARELO

    desenhar_botao(
        tela,
        botao_inicio_rect,
        cor_botao,
        PRETO,
        texto_botao,
        fonte_grande,
        PRETO,
        border_radius=20
    )


    # Imagem do troféu e de sair no canto inferior direito 
    espaco_entre = 20
    botao_creditos_rect = img_trofeu.get_rect()
    botao_sair_rect = img_sair.get_rect()

    botao_sair_rect.x = tela.get_width() - botao_sair_rect.width - 20
    botao_creditos_rect.x = botao_sair_rect.x - botao_creditos_rect.width - espaco_entre
    botao_sair_rect.y = botao_creditos_rect.y = tela.get_height() - botao_creditos_rect.height - 20

    tela.blit(img_trofeu, botao_creditos_rect.topleft)
    tela.blit(img_sair, botao_sair_rect.topleft)

    # Imagem da idade recomendada no canto inferior esquerdo
    img_idade_rect = img_idade.get_rect()
    img_idade_rect.x = 70
    img_idade_rect.y = tela.get_height() - 113
    tela.blit(img_idade, img_idade_rect.topleft)

    #Mudando o ponteiro do mouse
    mouse_pos = pygame.mouse.get_pos()

    if botao_creditos_rect.collidepoint(mouse_pos) or botao_sair_rect.collidepoint(mouse_pos) or botao_inicio_rect.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    elif caixa_texto.collidepoint(mouse_pos):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
    else:
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    # Retorne os retângulos dos botões para detecção de clique
    return botao_inicio_rect, botao_creditos_rect, botao_sair_rect

