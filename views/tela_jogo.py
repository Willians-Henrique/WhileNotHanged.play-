import string
import pygame

def desenhar_tela_jogo(tela, fontes, perguntas, cores, img_jogador, img_pontos,
                       img_relogio, img_vidas, img_voltar):
    # Fontes e cores
    fonte_pequena = fontes["pequena"]
    fonte_media = fontes["media"]
    fonte_grande = fontes["grande"]
    fonte_titulo = fontes["titulo"]

    AMARELO = cores["AMARELO"]
    PRETO = cores["PRETO"]
    AZUL = cores["AZUL"]

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
    base_y = ALTURA // 2 + 220  # Base posicionada um pouco abaixo do meio vertical

    # Base (horizontal)
    pygame.draw.rect(tela, PRETO, (base_x, base_y, base_largura, base_altura))

    # Poste (vertical)
    poste_x = base_x + base_largura // 2 - 10
    poste_y = base_y - poste_altura
    poste_largura = 20
    pygame.draw.rect(tela, PRETO, (poste_x, poste_y, poste_largura, poste_altura))

    # Braço horizontal
    braco_x = poste_x + poste_largura
    braco_y = poste_y
    braco_altura = 20
    pygame.draw.rect(tela, PRETO, (braco_x, braco_y, braco_largura, braco_altura))

    # Corda (linha)
    corda_x = braco_x + braco_largura
    corda_y_inicial = braco_y 
    pygame.draw.rect(tela, PRETO, (corda_x, corda_y_inicial, corda_largura, corda_altura))

    # --- Fim da forca ---

    # Voltar canto superior esquerdo
    img_voltar_rect = img_voltar.get_rect(topleft=(50, 30))
    tela.blit(img_voltar, img_voltar_rect)

    # Elementos canto superior direito
    espaco_horizontal = 200
    y_superior = 30

    img_vidas_rect = img_vidas.get_rect()
    img_vidas_rect.topright = (LARGURA - 150, y_superior)

    img_relogio_rect = img_relogio.get_rect()
    img_relogio_rect.topright = (img_vidas_rect.left - espaco_horizontal, y_superior)

    img_pontos_rect = img_pontos.get_rect()
    img_pontos_rect.topright = (img_relogio_rect.left - espaco_horizontal, y_superior)

    img_jogador_rect = img_jogador.get_rect()
    img_jogador_rect.topright = (img_pontos_rect.left - espaco_horizontal, y_superior)

    tela.blit(img_jogador, img_jogador_rect)
    tela.blit(img_pontos, img_pontos_rect)
    tela.blit(img_relogio, img_relogio_rect)
    tela.blit(img_vidas, img_vidas_rect)

    # Pergunta
    pergunta_atual = perguntas[7]  # ou [1] se quiser testar outra
    texto_pergunta = pergunta_atual["pergunta"]

    # Tamanho fixo do retângulo
    largura_ret = 723
    altura_ret = 150
    margem_direita = 100
    x_ret = LARGURA - largura_ret - margem_direita
    y_ret = 210

    # Desenha o retângulo amarelo fixo
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

    # Centraliza as linhas no retângulo
    total_altura_texto = sum(fonte_media.render(l, True, PRETO).get_height() for l in linhas if l)
    y_inicial_texto = y_ret + (altura_ret - total_altura_texto) // 2

    for i, linha in enumerate(linhas):
        if linha:
            texto_render = fonte_media.render(linha, True, PRETO)
            x_texto = x_ret + (largura_ret - texto_render.get_width()) // 2
            y_texto = y_inicial_texto + i * texto_render.get_height()
            tela.blit(texto_render, (x_texto, y_texto))

    # Palavra da forca
    palavra = pergunta_atual["resposta"].upper()
    letras_descobertas = pergunta_atual.get("descobertas", []) 

    num_letras = len(palavra)
    espaco_letra = 50
    largura_traco = 30

    x_inicial = x_ret + (largura_ret - (num_letras * espaco_letra)) // 2
    y_tracos = y_ret + altura_ret + 40

    for i, letra in enumerate(palavra):
        x = x_inicial + i * espaco_letra

        if letra in letras_descobertas:
            letra_render = fonte_grande.render(letra, True, PRETO)
        else:
            letra_render = fonte_grande.render("_", True, PRETO)

        x_letra = x + (largura_traco - letra_render.get_width()) // 2
        y_letra = y_tracos - letra_render.get_height() // 2
        tela.blit(letra_render, (x_letra, y_letra))

     
    # Desenha o alfabeto abaixo dos traços, alinhado para a direita (deslocado 800px da direita)
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

    return img_voltar_rect
