# esconder mensagem do pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import argparse
import sys
from core.app import App

if __name__ == '__main__':

    # ler argumentos do programa
    args = sys.argv[1:]
    
    parser = argparse.ArgumentParser("python src/main.py")
    parser.add_argument("--mode", help="Modo do app", choices=["dev", "build"], default="dev")
    args = parser.parse_args()
    
    # rodar jogo
    app = App(title='Naval Battle 2')
    app.run()