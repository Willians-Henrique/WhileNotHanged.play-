import pygame
import os

LARGURA = 1500
ALTURA = 800


CORES = {
    "BRANCO": (255, 255, 255),
    "PRETO": (0, 0, 0),
    "VERMELHO": (255, 50, 50),
    "VERDE": (50, 255, 50),
    "AZUL": (75,139,190),
    "AMARELO": (255,212,59),
    "AMARELO_HOVER": (255,232,115),
    "ROXO": (200, 0, 200),
    "LARANJA": (255, 150, 0),
    "ROSA": (255, 100, 180),
    "AZUL_CLARO": (173, 216, 230),
    "CINZA": (200, 200, 200),
    "marrom": (139, 69, 19),
    "pele": (255, 224, 189),  
    "preto": (0, 0, 0), 
}

IrishGrover = os.path.join("fonts", "IrishGrover-Regular.ttf")

# Definições de fontes
def get_fonts():
    try:
        print(f"Carregando fonte personalizada de: {IrishGrover}")
        return {
            "pequena": pygame.font.Font(IrishGrover, 24),
            "media": pygame.font.Font(IrishGrover, 32),
            "grande": pygame.font.Font(IrishGrover, 50),
            "titulo": pygame.font.Font(IrishGrover, 90),
        }
    except Exception as e:
        print(f"Erro ao carregar fonte personalizada: {e}")
        return {
            "pequena": pygame.font.SysFont(None, 24),
            "media": pygame.font.SysFont(None, 32, bold=True),
            "grande": pygame.font.SysFont(None, 48, bold=True),
            "titulo": pygame.font.SysFont(None, 64, bold=True),
        }

