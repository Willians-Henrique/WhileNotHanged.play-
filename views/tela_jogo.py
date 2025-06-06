import string
import pygame

def desenhar_tela_jogo(
    tela, fontes, textos, cores,
    nome_jogador, vidas, pontuacao, tempo_restante,
    pergunta_atual, perguntas, letras_adivinhadas, letras_disponiveis,
    erros_consecutivos, feedback,
    img_jogador, img_pontos, img_relogio, img_vidas, img_voltar
):
    # Fontes e cores
    fonte_pequena = fontes["pequena"]
    fonte_media = fontes["media"]
    fonte_grande = fontes["grande"]
    fonte_titulo = fontes.get("titulo", fonte_grande)

    AMARELO = cores["AMARELO"]
    PRETO = cores["PRETO"]
    AZUL = cores["AZUL"]
    BRANCO = cores.get("BRANCO", (255,255,255))
    VERMELHO = cores.get("VERMELHO", (255,0,0))
    VERDE = cores.get("VERDE", (0,255,0))
    ROXO = cores.get("ROXO", (128,0,128))

    LARGURA, ALTURA = tela.get_size()
    tela.fill(AZUL)

    # --- Desenha a forca no lado esquerdo ---
    base_largura = 200
    base_altura = 20
    poste_altura = 400
    braco_largura = 150
    corda_altura = 50
    corda_largura = 20

    base_x = 100
    base_y = ALTURA // 2 + 220

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

    # Voltar canto superior esquerdo
    img_voltar_rect = img_voltar.get_rect(topleft=(50, 30))
    tela.blit(img_voltar, img_voltar_rect)

    # Elementos canto superior direito (com texto ao lado dos ícones)
    espaco_horizontal = 200
    y_superior = 30

    # Vidas
    img_vidas_rect = img_vidas.get_rect()
    img_vidas_rect.topright = (LARGURA - 150, y_superior)
    tela.blit(img_vidas, img_vidas_rect)
    vidas_texto = fonte_media.render(str(vidas), True, VERMELHO)
    tela.blit(vidas_texto, (img_vidas_rect.left - 10 - vidas_texto.get_width(), y_superior + img_vidas_rect.height//2 - vidas_texto.get_height()//2))

    # Relógio
    img_relogio_rect = img_relogio.get_rect()
    img_relogio_rect.topright = (img_vidas_rect.left - espaco_horizontal, y_superior)
    tela.blit(img_relogio, img_relogio_rect)
    minutos = tempo_restante // 60
    segundos = tempo_restante % 60
    tempo_texto = fonte_media.render(f"{minutos:02d}:{segundos:02d}", True, VERDE)
    tela.blit(tempo_texto, (img_relogio_rect.left - 10 - tempo_texto.get_width(), y_superior + img_relogio_rect.height//2 - tempo_texto.get_height()//2))

    # Pontos
    img_pontos_rect = img_pontos.get_rect()
    img_pontos_rect.topright = (img_relogio_rect.left - espaco_horizontal, y_superior)
    tela.blit(img_pontos, img_pontos_rect)
    pontos_texto = fonte_media.render(str(pontuacao), True, AMARELO)
    tela.blit(pontos_texto, (img_pontos_rect.left - 10 - pontos_texto.get_width(), y_superior + img_pontos_rect.height//2 - pontos_texto.get_height()//2))

    # Jogador
    img_jogador_rect = img_jogador.get_rect()
    img_jogador_rect.topright = (img_pontos_rect.left - espaco_horizontal, y_superior)
    tela.blit(img_jogador, img_jogador_rect)
    nome_texto = fonte_media.render(nome_jogador, True, BRANCO)
    tela.blit(nome_texto, (img_jogador_rect.left - 10 - nome_texto.get_width(), y_superior + img_jogador_rect.height//2 - nome_texto.get_height()//2))

    # Pergunta
    pergunta = perguntas[pergunta_atual]
    texto_pergunta = pergunta["pergunta"]

    largura_ret = 723
    altura_ret = 150
    margem_direita = 100
    x_ret = LARGURA - largura_ret - margem_direita
    y_ret = 210

    pygame.draw.rect(
        tela, AMARELO,
        (x_ret, y_ret, largura_ret, altura_ret),
        border_radius=20
    )

    # Quebra de até 2 linhas
    palavras = texto_pergunta.split()
    linhas = ["", ""]
    idx = 0
    for palavra in palavras:
        tentativa = linhas[idx] + (" " if linhas[idx] else "") + palavra
        if fonte_media.render(tentativa, True, PRETO).get_width() <= largura_ret - 40:
            linhas[idx] = tentativa
        elif idx == 0:
            idx = 1
            linhas[idx] = palavra
        else:
            break

    total_altura_texto = sum(fonte_media.render(l, True, PRETO).get_height() for l in linhas if l)
    y_inicial_texto = y_ret + (altura_ret - total_altura_texto) // 2

    for i, linha in enumerate(linhas):
        if linha:
            texto_render = fonte_media.render(linha, True, PRETO)
            x_texto = x_ret + (largura_ret - texto_render.get_width()) // 2
            y_texto = y_inicial_texto + i * texto_render.get_height()
            tela.blit(texto_render, (x_texto, y_texto))

    # Palavra da forca
    palavra = pergunta["resposta"].upper()
    letras_descobertas = [l for l in letras_adivinhadas]  # lógica do seu jogo

    num_letras = len(palavra)
    espaco_letra = 50
    largura_traco = 30

    x_inicial = x_ret + (largura_ret - (num_letras * espaco_letra)) // 2
    y_tracos = y_ret + altura_ret + 40

    for i, letra in enumerate(palavra):
        x = x_inicial + i * espaco_letra
        if letra in letras_descobertas:
            letra_render = fonte_grande.render(letra, True, PRETO)
        elif letra == " ":
            letra_render = fonte_grande.render(" ", True, PRETO)
        else:
            letra_render = fonte_grande.render("_", True, PRETO)
        x_letra = x + (largura_traco - letra_render.get_width()) // 2
        y_letra = y_tracos - letra_render.get_height() // 2
        tela.blit(letra_render, (x_letra, y_letra))

    # Alfabeto
    alfabeto = list(string.ascii_uppercase)
    letras_por_linha = 10
    espacamento = 50
    largura_botao = 40
    altura_botao = 40

    x_alfabeto_inicial = LARGURA - 720
    margem_top = y_tracos + 60

    for i, letra in enumerate(alfabeto):
        linha = i // letras_por_linha
        coluna = i % letras_por_linha
        x = x_alfabeto_inicial + coluna * espacamento
        y = margem_top + linha * (altura_botao + 15)
        pygame.draw.rect(tela, AMARELO, (x, y, largura_botao, altura_botao), border_radius=8)
        letra_render = fonte_pequena.render(letra, True, PRETO)
        x_letra = x + (largura_botao - letra_render.get_width()) // 2
        y_letra = y + (altura_botao - letra_render.get_height()) // 2
        tela.blit(letra_render, (x_letra, y_letra))

    # Mensagem de cuidado
    if erros_consecutivos >= 2:
        cuidado_texto = fonte_grande.render(textos["cuidado"], True, VERMELHO)
        tela.blit(cuidado_texto, (x_ret, y_tracos + 120))

    # Dica se vidas <= 1
    if vidas <= 1:
        pygame.draw.rect(tela, AMARELO, (x_ret, y_tracos + 70, 800, 80), 0, border_radius=15)
        pygame.draw.rect(tela, PRETO, (x_ret, y_tracos + 70, 800, 80), 3, border_radius=15)
        texto_dica = fonte_pequena.render(textos["dica"].format(pergunta['dica']), True, PRETO)
        tela.blit(texto_dica, (x_ret + 20, y_tracos + 100))

    return img_voltar_rect