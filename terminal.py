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
    ║   3 ➜  Sobre                              ║
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
print("\nATENÇÃO: ShorKiller é apenas um projeto de estudos de Iniciação Científica.")
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
        print(f'''============================================================
SOBRE O PROGRAMA
============================================================
O ShorKiller foi desenvolvido com o objetivo de proporcionar uma 
melhor compreensão de conceitos de criptografia, algoritmos e 
computação quântica. O projeto contou com o apoio do programa de 
Iniciação Científica, que visa identificar vulnerabilidades na 
criptografia dos sistemas atuais diante do avanço da computação 
quântica e dos algoritmos viabilizados por ela.

============================================================
CONCEITOS: RSA
============================================================
O RSA é um protocolo de criptografia assimétrica amplamente 
utilizado na atualidade para garantir a segurança na troca de 
informações. Ele se baseia em duas chaves principais: a chave 
privada (d) e a chave pública (e).

1. GERAÇÃO DE CHAVES:
Para iniciar, utilizam-se dois fatores, 'p' e 'q', que devem ser 
obrigatoriamente números primos. Em seguida, calcula-se 'n':
    n = p × q

2. CÁLCULO DO TOTIENTE:
Deve-se calcular o totiente, também conhecido como variável 'z'. 
A fórmula é:
    z = (p - 1) × (q - 1)

3. DEFINIÇÃO DAS CHAVES (e, d):
- Chave Pública (e): Deve ser um número coprimo de 'z'. Ou seja, 
  o Máximo Divisor Comum (MDC) entre 'e' e 'z' deve ser igual a 1.
- Chave Privada (d): É o inverso multiplicativo modular de 'e', 
  calculada pela fórmula:
    d × e ≡ 1 mod(z)

4. PROCESSAMENTO DA MENSAGEM:
Para criptografar:
    (mensagem)ᵉ mod(n) = cripto

Para descriptografar:
    (cripto)ᵈ mod(n) = mensagem

------------------------------------------------------------
Finalizamos aqui os conceitos básicos da criptografia RSA, 
permitindo o avanço para o Algoritmo de Shor, responsável por 
sua quebra em um cenário de computação quântica.
============================================================''')
        input("Pressione ENTER para voltar ao menu principal.")

    elif acao == 4:
        print("ShorKiller encerrado.")
        break
    else:
        print("O valor inserido não é válido.")



