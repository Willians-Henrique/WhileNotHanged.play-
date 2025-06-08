class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.vidas = 3
        self.pontuacao = 0
        self.acertos_seguidos = 0
        self.erros_consecutivos = 0
        self.letras_adivinhadas = {}

    def adicionar_letra(self, letra):
        self.letras_adivinhadas.append(letra)

    def remover_vida(self):
        self.vidas -= 1

    def adicionar_pontuacao(self, valor=10):
        self.pontuacao += valor

    def resetar(self):
        self.vidas = 6
        self.pontuacao = 0
        self.acertos_seguidos = 0
        self.erros_consecutivos = 0
        self.letras_adivinhadas = {}

    def registrar_acerto(self):
        self.acertos_seguidos += 1
        self.erros_consecutivos = 0

    def registrar_erro(self):
        self.erros_consecutivos += 1
        self.acertos_seguidos = 0

    def verificar_letra_na_palavra(self, letra, palavra):
        if letra in palavra.upper():
            self.adicionar_letra(letra)
            self.registrar_acerto()
            self.adicionar_pontuacao()
            return True
        else:
            self.remover_vida()
            self.registrar_erro()
            return False