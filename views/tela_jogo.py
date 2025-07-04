import string
import pygame
from views.componentes import desenhar_forca


def desenhar_tela_jogo(
    tela, fontes, textos, cores,
    forca_game,
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

    # --- Dados do jogo via model ---
    nome_jogador = forca_game.jogador.nome if forca_game.jogador else ""
    vidas = forca_game.jogador.vidas if forca_game.jogador else 0
    pontuacao = forca_game.jogador.pontuacao if forca_game.jogador else 0
    tempo_restante = forca_game.tempo_restante
    pergunta = forca_game.get_pergunta_atual()
    resposta = forca_game.get_resposta_atual()
    dica = forca_game.get_dica_atual()
    letras_adivinhadas = forca_game.jogador.letras_adivinhadas if forca_game.jogador else []
    erros_consecutivos = forca_game.jogador.erros_consecutivos if forca_game.jogador else 0

  
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
    vidas_texto = fonte_grande.render(str(vidas), True, VERMELHO)
    tela.blit(vidas_texto, (img_vidas_rect.left + 130 - vidas_texto.get_width(), y_superior + img_vidas_rect.height//2 - vidas_texto.get_height()//2))

    # Relógio
    img_relogio_rect = img_relogio.get_rect()
    img_relogio_rect.topright = (img_vidas_rect.left - espaco_horizontal, y_superior)
    tela.blit(img_relogio, img_relogio_rect)
    minutos = tempo_restante // 60
    segundos = tempo_restante % 60
    tempo_texto = fonte_grande.render(f"{minutos:02d}:{segundos:02d}", True, VERDE)
    tela.blit(tempo_texto, (img_relogio_rect.left + 210 - tempo_texto.get_width(), y_superior + img_relogio_rect.height//2 - tempo_texto.get_height()//2))

    # Pontos
    img_pontos_rect = img_pontos.get_rect()
    img_pontos_rect.topright = (img_relogio_rect.left - espaco_horizontal, y_superior)
    tela.blit(img_pontos, img_pontos_rect)
    pontos_texto = fonte_grande.render(str(pontuacao), True, AMARELO)
    tela.blit(pontos_texto, (img_pontos_rect.left + 150 - pontos_texto.get_width(), y_superior + img_pontos_rect.height//2 - pontos_texto.get_height()//2))

    # Jogador
    img_jogador_rect = img_jogador.get_rect()
    img_jogador_rect.topright = (img_pontos_rect.left - 300, y_superior)
    tela.blit(img_jogador, img_jogador_rect)
    nome_texto = fonte_grande.render(nome_jogador, True, PRETO)
    tela.blit(nome_texto, ( img_jogador_rect.right + 10, y_superior + img_jogador_rect.height // 2 - nome_texto.get_height() // 2))

    # Pergunta
    texto_pergunta = pergunta.pergunta if pergunta else ""

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
    palavra = resposta
    letras_descobertas = [l for l in letras_adivinhadas]

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
        rect = pygame.Rect(x, y, largura_botao, altura_botao)

        cor_botao = AMARELO

        if letra in forca_game.jogador.letras_adivinhadas:
            if forca_game.jogador.letras_adivinhadas[letra]:
                cor_botao = VERDE
            else:
                cor_botao = VERMELHO

        pygame.draw.rect(tela, cor_botao, rect, border_radius=8)
        letra_texto = fonte_pequena.render(letra, True, PRETO)
        letra_rect = letra_texto.get_rect(center=rect.center)
        tela.blit(letra_texto, letra_rect)

    # Desenha a forca e o boneco conforme os erros
    erros = forca_game.erros_rodada
    desenhar_forca(tela, erros, cores=cores)

    # Mensagem de cuidado
    if dica:
        pygame.draw.rect(tela, AMARELO, (x_ret, y_tracos + 250, 800, 80), 0, border_radius=15)
        pygame.draw.rect(tela, PRETO, (x_ret, y_tracos + 250, 800, 80), 3, border_radius=15)
        texto_dica = fonte_pequena.render(textos["dica"].format(dica), True, PRETO)
        tela.blit(texto_dica, (x_ret + 20, y_tracos + 275))

    return img_voltar_rect