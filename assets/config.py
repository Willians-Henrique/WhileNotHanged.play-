import pygame

LARGURA = 1500
ALTURA = 800


CORES = {
    "BRANCO": (255, 255, 255),
    "PRETO": (0, 0, 0),
    "VERMELHO": (255, 50, 50),
    "VERDE": (50, 255, 50),
    "AZUL": (50, 50, 255),
    "AMARELO": (255, 255, 0),
    "ROXO": (200, 0, 200),
    "LARANJA": (255, 150, 0),
    "ROSA": (255, 100, 180),
    "AZUL_CLARO": (173, 216, 230),
    "CINZA": (200, 200, 200)
}


# Definições de fontes
def get_fonts():
    try:
        return {
            "pequena": pygame.font.SysFont('Comic Sans MS', 24),
            "media": pygame.font.SysFont('Comic Sans MS', 32, bold=True),
            "grande": pygame.font.SysFont('Comic Sans MS', 48, bold=True),
            "titulo": pygame.font.SysFont('Comic Sans MS', 64, bold=True),
        }
    except Exception:
        return {
            "pequena": pygame.font.SysFont(None, 24),
            "media": pygame.font.SysFont(None, 32, bold=True),
            "grande": pygame.font.SysFont(None, 48, bold=True),
            "titulo": pygame.font.SysFont(None, 64, bold=True),
        }
