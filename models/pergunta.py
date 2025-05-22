class Pergunta:
    def __init__(self, pergunta, resposta, dica):
        self.pergunta = pergunta
        self.resposta = resposta
        self.dica = dica

    def verificar_resposta(self, letra, letras_adivinhadas):
        """Verifica se a letra está na resposta e ainda não foi adivinhada."""
        letra = letra.upper()
        return letra in self.resposta.upper() and letra not in letras_adivinhadas

    def palavra_completa(self, letras_adivinhadas):
        """Verifica se todas as letras da resposta já foram adivinhadas."""
        for l in self.resposta.upper():
            if l != " " and l not in letras_adivinhadas:
                return False
        return True