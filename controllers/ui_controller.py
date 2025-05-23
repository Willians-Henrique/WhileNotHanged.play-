#Processa todos os eventos do pygame e delega ações para os outros controllers.
def processar_eventos(eventos, estado_jogo, ui, game, player, question):
    pass

#Desenha a tela de início usando os dados do jogador e UI.
def desenhar_tela_inicio(tela, fontes, textos, cores, ui, jogador):
    pass

#Desenha a tela do jogo.
def desenhar_tela_jogo(tela, fontes, textos, cores, ui, game, player, question):
    pass

#Desenha a tela de resultado.
def desenhar_tela_resultado(tela, fontes, textos, cores, ui, player, game):
    pass

#Desenha a tela de créditos.
def desenhar_tela_creditos(tela, fontes, textos, cores, ui):
    pass

def checar_clique_botao(event, botao_rect):
    if event.type == pygame.MOUSEBUTTONDOWN:
        if botao_rect.collidepoint(event.pos):
            print('Botão clicado!')
            return True
    return False