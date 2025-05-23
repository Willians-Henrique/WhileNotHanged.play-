from models.jogador import Jogador

#Cria e retorna um novo objeto Jogador.
def criar_jogador(nome=""):
    return Jogador(nome)

#Atualiza o nome do jogador conforme o evento de teclado.
def atualizar_nome(jogador, evento):
    if evento.key == 8:  # Backspace
        jogador.nome = jogador.nome[:-1]
    elif evento.key == 13:  # Enter
        jogador.nome = jogador.nome.strip()
    else:
        jogador.nome += evento.unicode

def adicionar_pontuacao(jogador, pontos):
    """Adiciona pontos ao jogador."""
    pass

def remover_vida(jogador):
    """Remove uma vida do jogador."""
    pass

def resetar_jogador(jogador):
    """Reseta o estado do jogador para um novo jogo."""
    pass