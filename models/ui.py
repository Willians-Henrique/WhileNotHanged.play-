import pygame

class UI:
    def __init__(self):
        self.botao_inicio = None
        self.botao_creditos = None
        self.botao_sair = None
        self.botao_reiniciar = None
        self.caixa_texto = None
        # Adicione outros elementos conforme necessário

    def desenhar_botao(self, tela, rect, cor, texto, fonte, cor_texto, border_radius=10):
        pygame.draw.rect(tela, cor, rect, 0, border_radius=border_radius)
        pygame.draw.rect(tela, (0, 0, 0), rect, 3, border_radius=border_radius)
        texto_render = fonte.render(texto, True, cor_texto)
        tela.blit(
            texto_render,
            (rect.x + rect.width // 2 - texto_render.get_width() // 2,
             rect.y + rect.height // 2 - texto_render.get_height() // 2)
        )

    def desenhar_caixa_texto(self, tela, rect, cor, ativo, fonte, texto, cor_texto):
        pygame.draw.rect(tela, cor, rect, 0, border_radius=15)
        pygame.draw.rect(tela, (0, 0, 0), rect, 3, border_radius=15)
        texto_render = fonte.render(texto, True, cor_texto)
        tela.blit(texto_render, (rect.x + 20, rect.y + 15))

    def verificar_clique(self, rect, pos):
        return rect.collidepoint(pos)