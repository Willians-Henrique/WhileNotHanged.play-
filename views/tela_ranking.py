import pygame

def desenhar_tela_ranking(tela, fontes, textos, cores, img_voltar):
    # Desempacota as fontes e cores
    fonte_grande = fontes["grande"]
    fonte_titulo = fontes["titulo"]


    PRETO = cores["PRETO"]
    AZUL = cores["AZUL"]

    LARGURA, ALTURA = tela.get_size()

    # Fundo azul
    tela.fill(AZUL)

    # Título
    titulo = fonte_titulo.render(textos["creditos"], True, PRETO)
    tela.blit(titulo, (LARGURA//2 - titulo.get_width()//2, 30))


    # Lista de jogadores e pontuações
    ranking = [("Eliseu", 10), ("Willians", 9), ("Eduarda", 8), ("Kaue", 7)
    ]

    y_pos = 150
    margem_esquerda = 300
    margem_direita = LARGURA - 300

    for nome, pontos in ranking:
        texto_nome = fonte_grande.render(nome, True, PRETO)
        texto_pontos = fonte_grande.render(f"{pontos:02d} pontos", True, PRETO)

        # Alinha o nome à esquerda e os pontos à direita
        tela.blit(texto_nome, (margem_esquerda, y_pos))
        tela.blit(texto_pontos, (margem_direita - texto_pontos.get_width(), y_pos))

        y_pos += 70

    # Posição do jogador atual
    posicao_jogador = fonte_grande.render(textos["posicao"], True, PRETO)
    tela.blit(posicao_jogador, (LARGURA//2 - posicao_jogador.get_width()//2, 530))

    # Botão Voltar
    botao_voltar_rect = img_voltar.get_rect(center=(LARGURA//2, ALTURA - 100))
    tela.blit(img_voltar, botao_voltar_rect)

    return botao_voltar_rect