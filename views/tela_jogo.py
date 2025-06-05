import pygame

def desenhar_tela_jogo(
    tela, fontes, textos, cores,
    nome_jogador, vidas, pontuacao, tempo_restante,
    pergunta_atual, perguntas, letras_adivinhadas, letras_disponiveis,
    erros_consecutivos, feedback, y=300
):
    # Desempacota as fontes e cores
    fonte_pequena = fontes["pequena"]
    fonte_media = fontes["media"]
    fonte_grande = fontes["grande"]

    BRANCO = cores["BRANCO"]
    PRETO = cores["PRETO"]
    VERMELHO = cores["VERMELHO"]
    VERDE = cores["VERDE"]
    AZUL = cores["AZUL"]
    AMARELO = cores["AMARELO"]
    ROXO = cores["ROXO"]
    ROSA = cores["ROSA"]
    LARANJA = cores["LARANJA"]
    AZUL_CLARO = cores["AZUL_CLARO"]

    LARGURA, ALTURA = tela.get_size()

    # Fundo
    tela.fill(AZUL_CLARO)

    # Cabeçalho
    pygame.draw.rect(tela, AZUL, (0, 0, LARGURA, 100))
    nome_texto = fonte_media.render(textos["jogador"].format(nome_jogador), True, BRANCO)
    tela.blit(nome_texto, (20, 30))
    vidas_texto = fonte_media.render(textos["vidas"].format(vidas), True, VERMELHO)
    tela.blit(vidas_texto, (LARGURA - 200, 30))
    pontos_texto = fonte_media.render(textos["pontos"].format(pontuacao), True, AMARELO)
    tela.blit(pontos_texto, (LARGURA//2 - pontos_texto.get_width()//2, 30))

    # Temporizador
    minutos = tempo_restante // 60
    segundos = tempo_restante % 60
    tempo_texto = fonte_media.render(textos["tempo"].format(minutos, segundos), True, VERDE)
    tela.blit(tempo_texto, (LARGURA - 600, 30))

    # Área da forca
    pygame.draw.rect(tela, BRANCO, (50, 120, 500, 500), border_radius=20)
    pygame.draw.rect(tela, PRETO, (50, 120, 500, 500), 3, border_radius=20)

    # Desenhar forca e boneco
    FORCA_X, FORCA_Y = 100, 150
    partes_forca = [
        lambda: pygame.draw.rect(tela, (139, 69, 19), (FORCA_X-20, FORCA_Y+300, 300, 30)),
        lambda: pygame.draw.rect(tela, (139, 69, 19), (FORCA_X+120, FORCA_Y+50, 20, 250)),
        lambda: pygame.draw.rect(tela, (139, 69, 19), (FORCA_X+120, FORCA_Y+50, 150, 20)),
        lambda: pygame.draw.rect(tela, (139, 69, 19), (FORCA_X+260, FORCA_Y+50, 10, 50)),
        lambda: [
            pygame.draw.circle(tela, (255, 218, 185), (FORCA_X+265, FORCA_Y+125), 25),
            pygame.draw.circle(tela, PRETO, (FORCA_X+255, FORCA_Y+120), 3),
            pygame.draw.circle(tela, PRETO, (FORCA_X+275, FORCA_Y+120), 3),
            pygame.draw.line(tela, PRETO, (FORCA_X+255, FORCA_Y+140), (FORCA_X+275, FORCA_Y+140), 2)
        ],
        lambda: pygame.draw.line(tela, (255, 218, 185), (FORCA_X+265, FORCA_Y+150), (FORCA_X+265, FORCA_Y+250), 5),
        lambda: pygame.draw.line(tela, (255, 218, 185), (FORCA_X+265, FORCA_Y+170), (FORCA_X+230, FORCA_Y+200), 5),
        lambda: pygame.draw.line(tela, (255, 218, 185), (FORCA_X+265, FORCA_Y+170), (FORCA_X+300, FORCA_Y+200), 5),
        lambda: pygame.draw.line(tela, (255, 218, 185), (FORCA_X+265, FORCA_Y+250), (FORCA_X+240, FORCA_Y+300), 5),
        lambda: pygame.draw.line(tela, (255, 218, 185), (FORCA_X+265, FORCA_Y+250), (FORCA_X+290, FORCA_Y+300), 5)
    ]
    # Estrutura da forca
    for i in range(4):
        partes_forca[i]()
    # Boneco conforme erros
    erros = max(0, 6 - vidas)
    for i in range(4, 4 + min(erros, 6)):
        parte = partes_forca[i]
        resultado = parte()
        if isinstance(resultado, list):
            for elemento in resultado:
                if callable(elemento):
                    elemento()

    # Área da pergunta e opções
    pygame.draw.rect(tela, BRANCO, (600, 120, 850, 500), border_radius=20)
    pygame.draw.rect(tela, PRETO, (600, 120, 850, 500), 3, border_radius=20)

    # Mensagem de cuidado
    if erros_consecutivos >= 2:
        cuidado_texto = fonte_grande.render(textos["cuidado"], True, VERMELHO)
        tela.blit(cuidado_texto, (620, 650))

    # Pergunta (com quebra de linha se necessário)
    pergunta = perguntas[pergunta_atual]
    texto_pergunta = fonte_media.render(pergunta["pergunta"], True, PRETO)
    if texto_pergunta.get_width() <= 800:
        tela.blit(texto_pergunta, (620, 150))
    else:
        palavras = pergunta["pergunta"].split()
        linha1, linha2 = "", ""
        for palavra in palavras:
            if fonte_media.render(linha1 + " " + palavra, True, PRETO).get_width() <= 800:
                if linha1:
                    linha1 += " " + palavra
                else:
                    linha1 = palavra
            else:
                linha2 += " " + palavra
        tela.blit(fonte_media.render(linha1, True, PRETO), (620, 140))
        tela.blit(fonte_media.render(linha2, True, PRETO), (620, 180))

    # Palavra escondida
    letras = []
    for letra in pergunta["resposta"]:
        if letra == " ":
            letras.append(" ")
        elif letra.upper() in letras_adivinhadas:
            letras.append(letra.upper())
        else:
            letras.append("_")
    texto_palavra = fonte_grande.render(" ".join(letras), True, PRETO)
    tela.blit(texto_palavra, (620, 200))

    # Letras disponíveis
    texto_instrucao = fonte_media.render(textos["selecione_letra"], True, PRETO)
    tela.blit(texto_instrucao, (620, 250))
    x, y_letra = 620, 300
    for i, letra in enumerate(letras_disponiveis):
        if i % 10 == 0 and i > 0:
            x = 620
            y_letra += 70
        cor = VERDE if letra in letras_adivinhadas else ROXO
        retangulo = pygame.Rect(x, y_letra, 50, 50)
        pygame.draw.rect(tela, cor, retangulo, 0, border_radius=10)
        pygame.draw.rect(tela, PRETO, retangulo, 3, border_radius=10)
        texto_letra = fonte_media.render(letra, True, BRANCO)
        tela.blit(texto_letra, (x + 25 - texto_letra.get_width()//2, y_letra + 25 - texto_letra.get_height()//2))
        x += 70

    # Dica se vidas <= 1
    if vidas <= 1:
        pygame.draw.rect(tela, AMARELO, (620, y + 70, 800, 80), 0, border_radius=15)
        pygame.draw.rect(tela, PRETO, (620, y + 70, 800, 80), 3, border_radius=15)
        texto_dica = fonte_pequena.render(textos["dica"].format(pergunta['dica']), True, PRETO)
        tela.blit(texto_dica, (640, y + 100))