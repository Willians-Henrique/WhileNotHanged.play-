import pygame

def desenhar_tela_inicio(
    tela, fontes, textos, cores, 
    input_ativo, caixa_texto, nome_jogador
):
    # Desempacota as fontes e cores
    fonte_pequena = fontes["pequena"]
    fonte_media = fontes["media"]
    fonte_grande = fontes["grande"]
    fonte_titulo = fontes["titulo"]

    BRANCO = cores["BRANCO"]
    PRETO = cores["PRETO"]
    ROSA = cores["ROSA"]
    ROXO = cores["ROXO"]
    LARANJA = cores["LARANJA"]
    CINZA = cores["CINZA"]
    AZUL = cores["AZUL"]
    VERMELHO = cores["VERMELHO"]
    AZUL_CLARO = cores["AZUL_CLARO"]

    LARGURA, ALTURA = tela.get_size()

    # Fundo animado (pode ser função separada)
    tela.fill(AZUL_CLARO)
    s = pygame.Surface((LARGURA, ALTURA), pygame.SRCALPHA)
    pygame.draw.rect(s, (173, 216, 230, 150), (0, 0, LARGURA, ALTURA))
    tela.blit(s, (0, 0))

    titulo = fonte_titulo.render(textos["titulo"], True, PRETO)
    pygame.draw.rect(tela, BRANCO, (LARGURA//2 - titulo.get_width()//2 - 20, 80, 
                                  titulo.get_width() + 40, titulo.get_height() + 40), 
                                  border_radius=20)
    tela.blit(titulo, (LARGURA//2 - titulo.get_width()//2, 100))

    subtitulo = fonte_media.render(textos["subtitulo"], True, PRETO)
    tela.blit(subtitulo, (LARGURA//2 - subtitulo.get_width()//2, 180))

    pygame.draw.rect(tela, ROSA if input_ativo else ROXO, caixa_texto, 0, border_radius=15)
    pygame.draw.rect(tela, PRETO, caixa_texto, 3, border_radius=15)

    texto_nome = fonte_media.render(textos["digite_nome"], True, PRETO)
    tela.blit(texto_nome, (caixa_texto.x, caixa_texto.y - 40))

    texto_input = fonte_media.render(nome_jogador, True, PRETO)
    tela.blit(texto_input, (caixa_texto.x + 20, caixa_texto.y + 15))

    texto_botao = fonte_grande.render(textos["comecar"], True, PRETO)
    largura_botao = max(240, texto_botao.get_width() + 60)
    botao_inicio_rect = pygame.Rect(LARGURA//2 - largura_botao//2, ALTURA//2 + 150, largura_botao, 70)

    pygame.draw.rect(tela, LARANJA, botao_inicio_rect, 0, border_radius=20)
    pygame.draw.rect(tela, PRETO, botao_inicio_rect, 3, border_radius=20)
    tela.blit(texto_botao, (botao_inicio_rect.x + largura_botao//2 - texto_botao.get_width()//2, 
                          botao_inicio_rect.y + 35 - texto_botao.get_height()//2))

    botao_creditos_rect = pygame.Rect(50, ALTURA - 110, 150, 50)
    pygame.draw.rect(tela, CINZA, botao_creditos_rect, 0, border_radius=10)
    pygame.draw.rect(tela, PRETO, botao_creditos_rect, 3, border_radius=10)

    texto_creditos = fonte_pequena.render(textos["creditos"], True, PRETO)
    tela.blit(texto_creditos, (botao_creditos_rect.x + 75 - texto_creditos.get_width()//2, 
                             botao_creditos_rect.y + 25 - texto_creditos.get_height()//2))

    botao_sair_rect = pygame.Rect(LARGURA - 200, ALTURA - 80, 150, 50)
    pygame.draw.rect(tela, CINZA, botao_sair_rect, 0, border_radius=10)
    pygame.draw.rect(tela, PRETO, botao_sair_rect, 3, border_radius=10)
    texto_sair = fonte_media.render(textos["sair_jogo"], True, VERMELHO)
    tela.blit(texto_sair, (botao_sair_rect.x + 75 - texto_sair.get_width()//2, 
                         botao_sair_rect.y + 25 - texto_sair.get_height()//2))

    pygame.draw.rect(tela, AZUL, (0, ALTURA-60, LARGURA, 60))
    idade = fonte_pequena.render(textos["idade"], True, BRANCO)
    tela.blit(idade, (LARGURA//2 - idade.get_width()//2, ALTURA - 40))

    # Retorne os retângulos dos botões para detecção de clique
    return botao_inicio_rect, botao_creditos_rect, botao_sair_rect