from models.jogador import Jogador
from models.pergunta import Pergunta

class ForcaGame:
    def __init__(self, perguntas):
        self.jogador = None  # Instância de Jogador
        self.perguntas = perguntas  # Lista de Pergunta
        self.pergunta_atual = 0
        self.tempo_restante = 120
        self.estado_jogo = 0
        self.feedback = ""
        self.dica_mostrada = False
        self.letras_disponiveis = [chr(i) for i in range(65, 91)]
        self.letras_rect = []
        self.mostrar_creditos = False

    def iniciar(self, nome_jogador):
        self.jogador = Jogador(nome_jogador)
        self.pergunta_atual = 0
        self.tempo_restante = 120
        self.feedback = ""
        self.dica_mostrada = False
        self.letras_disponiveis = [chr(i) for i in range(65, 91)]
        self.letras_rect = []
        self.mostrar_creditos = False

    def proxima_pergunta(self):
        self.pergunta_atual += 1
        self.tempo_restante = 120
        self.feedback = ""
        self.dica_mostrada = False
        self.jogador.letras_adivinhadas = []

    def verificar_letra(self, letra):
        pergunta = self.perguntas[self.pergunta_atual]
        if pergunta.verificar_resposta(letra, self.jogador.letras_adivinhadas):
            self.jogador.adicionar_letra(letra)
            if pergunta.palavra_completa(self.jogador.letras_adivinhadas):
                self.feedback = "correto"
                self.jogador.adicionar_pontuacao()
                self.dica_mostrada = False
                self.jogador.registrar_acerto()
            return True
        else:
            self.feedback = "errado"
            self.jogador.remover_vida()
            self.jogador.registrar_erro()
            return False

    def reiniciar(self):
        if self.jogador:
            self.jogador.resetar()
        self.pergunta_atual = 0
        self.tempo_restante = 120
        self.feedback = ""
        self.dica_mostrada = False
        self.letras_disponiveis = [chr(i) for i in range(65, 91)]
        self.letras_rect = []
        self.mostrar_creditos = False

    def atualizar_tempo(self):
        if self.tempo_restante > 0:
            self.tempo_restante -= 1
        else:
            self.jogador.remover_vida()
            self.feedback = "errado"

    def processar_evento(self, evento):
        # Aqui você pode implementar o processamento de eventos do pygame
        pass

    def desenhar_tela(self):
        # Aqui você pode chamar as funções de view para desenhar a tela
        pass

    def desenhar_forca(self):
        # Aqui você pode chamar a função de desenhar a forca
        pass