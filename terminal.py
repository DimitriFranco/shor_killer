import shor_prototype
import rsa_prototype
import util

def menu_acao():    
    print(r'''
    ╔═══════════════════════════════════════════╗
    ║           SHOR PROTOTYPE v1.0             ║
    ╠═══════════════════════════════════════════╣
    ║                                           ║
    ║   1 ➜  RSA                                ║
    ║   2 ➜  Shor Algorithm                     ║ 
    ║   3 ➜  Números de Teste                   ║
    ║   4 ➜  Sair                               ║
    ║                                           ║
    ╚═══════════════════════════════════════════╝
    ''')


#util.limpar_tela()
print("Inicializando ShorKiller...")
util.loading_spinner(3, "Carregando")
print(r'''┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                                                                                │
│                                                                                                                │
│   ________  ___  ___  ________  ________          ___  __    ___  ___       ___       _______   ________       │
│  |\   ____\|\  \|\  \|\   __  \|\   __  \        |\  \|\  \ |\  \|\  \     |\  \     |\  ___ \ |\   __  \      │
│  \ \  \___|\ \  \\\  \ \  \|\  \ \  \|\  \       \ \  \/  /|\ \  \ \  \    \ \  \    \ \   __/|\ \  \|\  \     │
│   \ \_____  \ \   __  \ \  \\\  \ \   _  _\       \ \   ___  \ \  \ \  \    \ \  \    \ \  \_|/_\ \   _  _\    │
│    \|____|\  \ \  \ \  \ \  \\\  \ \  \\  \|       \ \  \\ \  \ \  \ \  \____\ \  \____\ \  \_|\ \ \  \\  \|   │
│      ____\_\  \ \__\ \__\ \_______\ \__\\ _\        \ \__\\ \__\ \__\ \_______\ \_______\ \_______\ \__\\ _\   │
│     |\_________\|__|\|__|\|_______|\|__|\|__|        \|__| \|__|\|__|\|_______|\|_______|\|_______|\|__|\|__|  │
│     \|_________|                                                                                               │
│                                                                                                                │
│                                                                                                                │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘''')
print("\nATENÇÃO: ShorKiller é um projeto de estudos utilizado apenas para testes de quebra de criptografia por meio da computação quântica. Não deve ser utilizado de forma maliciosa.")
print("Feito por: Dimitri Franco")

while True:      
    menu_acao()
    acao = int(input("Digite sua ação a seguir: "))
    if acao == 1:
        util.loading_spinner(2, "Abrindo Simulador de RSA")
        rsa_prototype.rsa_program()
        input("Pressione ENTER para voltar ao menu principal.")
    elif acao == 2:
        util.loading_spinner(2, "Abrindo Simulador de Shor")
        shor_prototype.shor_program()
        input("Pressione ENTER para voltar ao menu principal.")
    elif acao == 3:
        print("A ser concluído")
    elif acao == 4:
        print("ShorKiller encerrado.")
        break
    else:
        print("O valor inserido não é válido.")



