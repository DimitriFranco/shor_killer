import time
import os
import sys

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_spinner(segundos, palavra):
    frames = ['-', '\\', '|', '/']
    iteracoes = segundos * 10

    for i in range(int(iteracoes)):
        frame = frames[i % len(frames)] 
        print(f"\r{palavra}... {frame}", end="")
        sys.stdout.flush() 
        time.sleep(0.1)
    print("\rConcluído!                                          ") 
