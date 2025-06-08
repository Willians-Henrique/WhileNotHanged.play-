from models.jogador import Jogador
from models.pergunta import Pergunta

class ForcaGame:
    def __init__(self, perguntas):
        self.jogador = None  # Instância de Jogador
        self.perguntas = [
            Pergunta(
                p["pergunta"],
                p["resposta"],
                p["dicas"] if "dicas" in p and p["dicas"] else []
            ) if isinstance(p, dict) else p
            for p in perguntas
                ]
        self.pergunta_atual = 0
        self.tempo_restante = 120
        self.estado_jogo = 0
        self.erros_rodada = 0
        self.dica_timer1 = 0
        self.dica_timer2 = 0
        self.avancar_proxima = False
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
        self.jogador.letras_adivinhadas = {}
        self.erros_rodada = 0
        self.dica_timer1 = 0
        self.dica_timer2 = 0

    def verificar_letra(self, letra):
        pergunta = self.perguntas[self.pergunta_atual]
        letra = letra.upper()
        letra_correta = pergunta.verificar_resposta(letra, self.jogador.letras_adivinhadas)

        self.jogador.letras_adivinhadas[letra] = letra_correta  # Armazena se acertou ou não

        if letra_correta:
            if pergunta.palavra_completa(self.jogador.letras_adivinhadas):
                self.feedback = "correto"
                self.jogador.adicionar_pontuacao()
                self.dica_mostrada = False
                self.jogador.registrar_acerto()
                self.avancar_proxima = True
            return True
        else:
            self.feedback = "errado"
            self.erros_rodada += 1
            self.jogador.registrar_erro()
            if self.erros_rodada == 2:
                self.dica_timer1 = 5
            if self.erros_rodada == 4:
                self.dica_timer2 = 5
            if self.erros_rodada >= 6:
                self.jogador.remover_vida()
                self.erros_rodada = 0
                self.avancar_proxima = True
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
        self.erros_rodada = 0
        self.dica_timer1 = 0
        self.dica_timer2 = 0

    def atualizar_tempo(self):
        if self.tempo_restante > 0:
            self.tempo_restante -= 1
        else:
            self.jogador.remover_vida()
            self.feedback = "Tempo esgotado!"
        # Atualiza o timer da dica
        if self.dica_timer1 > 0:
            self.dica_timer1 -= 1
        if self.dica_timer2 > 0:
            self.dica_timer2 -= 1
    def get_pergunta_atual(self):
        if 0 <= self.pergunta_atual < len(self.perguntas):
            return self.perguntas[self.pergunta_atual]
        return None

    
    def get_resposta_atual(self):
        pergunta = self.get_pergunta_atual()
        if pergunta:
            return pergunta.resposta.upper()
        return ""

    def get_dica_atual(self):
        pergunta = self.get_pergunta_atual()
        if not pergunta or not hasattr(pergunta, "dicas"):
            return ""
        # Segunda dica tem prioridade se timer ativo
        if self.dica_timer2 > 0 and len(pergunta.dicas) > 1:
            return pergunta.dicas[1]
        # Primeira dica
        if self.dica_timer1 > 0 and len(pergunta.dicas) > 0:
            return pergunta.dicas[0]
        return ""

    def get_num_perguntas(self):
        return len(self.perguntas)

    def processar_evento(self, evento):
        # Aqui você pode implementar o processamento de eventos do pygame
        pass

    def desenhar_tela(self):
        # Aqui você pode chamar as funções de view para desenhar a tela
        pass

    def desenhar_forca(self):
        # Aqui você pode chamar a função de desenhar a forca
        pass