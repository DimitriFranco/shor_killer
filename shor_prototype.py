import util

def euclides_diagram(dividendo, divisor, search = False):
    resto = -1
    dvd = dividendo
    dvs = divisor
    while resto != 0:
        #print( dvd, dvs, resto)
        resto = dvd % dvs
        dvd = dvs
        if resto != 0:
            dvs = resto
    if dvs == 1:
        if search:
            return dvs
        #resultado = "Os números " + str(dividendo) + " e " + str(divisor) + " são números coprimos."
        resultado = divisor
        return resultado
    else:
        if search:
            return dvs
        #resultado = "Não são coprimos."
        resultado = 0
        return resultado


def shor_program():
    print(r'''╔══════════════════════════════════════════════════════════════════════════════╗
║ ____  _   _  ___  ____    ____ ___ __  __ _   _ _        _  _____ ___  ____  ║
║/ ___|| | | |/ _ \|  _ \  / ___|_ _|  \/  | | | | |      / \|_   _/ _ \|  _ \ ║
║\___ \| |_| | | | | |_) | \___ \| || |\/| | | | | |     / _ \ | || | | | |_) |║
║ ___) |  _  | |_| |  _ <   ___) | || |  | | |_| | |___ / ___ \| || |_| |  _ < ║
║|____/|_| |_|\___/|_| \_\ |____/___|_|  |_|\___/|_____/_/   \_\_| \___/|_| \_\║
╚══════════════════════════════════════════════════════════════════════════════╝''')

    util.loading_spinner(2, "Carregando")    
    n = int(input("- Digite um valor para a variante N: "))
    util.loading_spinner(3, "Processando dados")
    #escolher a, 1 < a < N
    #verificar se a é coprimo de N
    lista_a = []
    for i in range(22, n):
        a = euclides_diagram(n, i)
        if a:
            lista_a.append(a)
            continue
    #print(lista_a)


    #utilizar a função if a^r % N == 1
    #também r tem que ser par, e a^(r/2) % N != -1
    matriz_r = []
    for num in lista_a:
        lista_r = []
        for r in range(1,30):
            if r % 2 != 0:
                continue
            if (num**r) % n == 1:
                if (num**(r/2)) % n == 1:
                    continue
            lista_r.append(r)
            continue
        matriz_r.append(lista_r)
    #print(matriz_r)


    #por fim, mdc((a^(r/2) +- 1), N)
    #o resultado com o + é o p, e o com - é o q
    reg_p = 0
    reg_q = 0
    for i in range(len(lista_a)):
        for l in range(len(matriz_r[i])):
            new_a = lista_a[i] ** (matriz_r[i][l] / 2)
            p = euclides_diagram(new_a - 1, n, True)
            q = euclides_diagram(new_a + 1, n, True)
            if p == 1 or p == n or q == 1 or q == n:
                continue
            else:
                #print("p =", p, "q =", q)
                if reg_p == 0:
                    reg_p = p 
                elif reg_p != p:
                    reg_q = p 
            break
        if reg_p and reg_q:
                break
    
    util.loading_spinner(2, "Carregando resultados")
    print(f"""
    ╔══════════════════════════════════════════╗
    ║        RESULTS: QUANTUM ANALYSIS         ║
    ╠══════════════════════════════════════════╣
    ║                                          ║
    ║   > FATOR P: {int(reg_p):<19}         ║
    ║   > FATOR Q: {int(reg_q):<19}         ║
    ║                                          ║
    ╠══════════════════════════════════════════╣
    ║         ENCRYPTION KEY BROKEN            ║
    ╚══════════════════════════════════════════╝
""")
    
    find_d = input("- Deseja descobrir a chave privada? (y/n) ")
    # for i in range(len(lista_a)):
    #     for l in range(len(matriz_r[i])):
    #         new_a = lista_a[i] ** (matriz_r[i][l] / 2)
    #         p = euclides_diagram(new_a - 1, n, True)
    #         q = euclides_diagram(new_a + 1, n, True)
    #         if p == 1 or p == n and q == 1 or q == n:
    #             continue
    #         else:
    #             print("p =", p, "q =", q)

