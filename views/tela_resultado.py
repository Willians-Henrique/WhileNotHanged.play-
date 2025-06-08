import pygame

def desenhar_tela_resultado(tela, fontes, textos, cores, btn_reiniciar, btn_sair, pontuacao, perguntas):
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
    
    pygame.draw.rect(tela, BRANCO, (LARGURA//2 - 400, ALTURA//2 - 250, 800, 500), border_radius=30)
    pygame.draw.rect(tela, PRETO, (LARGURA//2 - 400, ALTURA//2 - 250, 800, 500), 3, border_radius=30)
    
    titulo = fonte_titulo.render(textos["fim_jogo"], True, VERMELHO)
    tela.blit(titulo, (LARGURA//2 - titulo.get_width()//2, ALTURA//2 - 200))
    
    acertos = pontuacao // 10
    resultado_texto = fonte_grande.render(textos["pontuacao"].format(pontuacao), True, PRETO)
    tela.blit(resultado_texto, (LARGURA//2 - resultado_texto.get_width()//2, ALTURA//2 - 100))
    
    desempenho = fonte_media.render(textos["acertos"].format(acertos, len(perguntas)), True, PRETO)
    tela.blit(desempenho, (LARGURA//2 - desempenho.get_width()//2, ALTURA//2 - 30))
    
    if acertos >= len(perguntas) * 0.7:
        mensagem = fonte_media.render(textos["mensagem_vitoria"], True, AMARELO)
    else:
        mensagem = fonte_media.render(textos["mensagem_derrota"], True, AMARELO)
    tela.blit(mensagem, (LARGURA//2 - mensagem.get_width()//2, ALTURA//2 + 30))
    
    botao_reiniciar = pygame.Rect(LARGURA//2 - 150, ALTURA//2 + 100, 300, 70)
    texto_botao = fonte_grande.render(textos["jogar_novamente"], True, VERDE)
    tela.blit(texto_botao, (botao_reiniciar.x + 150 - texto_botao.get_width()//2, 
                           botao_reiniciar.y + 35 - texto_botao.get_height()//2))
    
    botao_sair = pygame.Rect(LARGURA - 200, ALTURA - 80, 150, 50)
    texto_sair = fonte_media.render(textos["sair_jogo"], True, VERMELHO)
    tela.blit(texto_sair, (botao_sair.x + 75 - texto_sair.get_width()//2, 
                         botao_sair.y + 25 - texto_sair.get_height()//2))
    
    return botao_reiniciar, botao_sair
