import pyperclip
import util
def vef_primo(q):
    i = 2
    resultado = True
    while i <= (q ** 0.5):
        if q % i == 0:
            resultado = False
            break
        i += 1
    return resultado

def msg_primo(resultado, q):
    if resultado:
        print("Sys:", str(q), "foi verificado como número primo.")
        return True
    else: 
        print("O número digitado não se configura como número primo, tente novamente.")
        return False

def euclides_diagram(dividendo, divisor):
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
        #resultado = "Os números " + str(dividendo) + " e " + str(divisor) + " são números coprimos."
        resultado = divisor
        return resultado
    else:
        #resultado = "Não são coprimos."
        resultado = 0
        return resultado

def find_d(e, z):
    d = 0
    for i in range(1, z):
        if (i * e) % z == 1 and i != e:
            d = i
            break
    if d:
        return d
    else:
        return "Não encontrado"
    
def defin_n(p, q):
    num = p * q
    return num

def defin_z(p, q):
    num = (p - 1) * (q - 1)
    return num

def msg_to_ascii(mensagem):
    list_ascii = []
    for letter in mensagem.upper():
        ascii_letter = ord(letter)
        list_ascii.append(ascii_letter)
    return list_ascii

def ascii_to_crypt(list_ascii, e, n):
    list_crypt = []
    for i in list_ascii:
        crypt_char = (i ** e) % n
        list_crypt.append(crypt_char)
    return list_crypt

def crypt_to_ascii(list_crypt, d, n):
    list_ascii = []
    for i in list_crypt:
        ascii_char = (i ** d) % n
        list_ascii.append(ascii_char)
    return list_ascii

def ascii_to_msg(list_ascii):
    msg = ""
    for char in list_ascii:
        msg += chr(char)
    return msg

def rsa_program():
    loop_primo = True
    print(r'''╔═════════════════════════════════════════════════════════════════════════╗
║ ____  ____    _      ____ ___ __  __ _   _ _        _  _____ ___  ____  ║
║|  _ \/ ___|  / \    / ___|_ _|  \/  | | | | |      / \|_   _/ _ \|  _ \ ║
║| |_) \___ \ / _ \   \___ \| || |\/| | | | | |     / _ \ | || | | | |_) |║
║|  _ < ___) / ___ \   ___) | || |  | | |_| | |___ / ___ \| || |_| |  _ < ║
║|_| \_\____/_/   \_\ |____/___|_|  |_|\___/|_____/_/   \_\_| \___/|_| \_\║
╚═════════════════════════════════════════════════════════════════════════╝''')
    util.loading_spinner(2, "Carregando")    

    while loop_primo:
        q = int(input("- Digite um número primo para a variável \"Q\": "))
        loop_primo = not msg_primo(vef_primo(q), q)
        
    loop_primo = True
    while loop_primo:
        p = int(input("- Digite um número primo para a variável \"P\": "))
        loop_primo = not msg_primo(vef_primo(p), p)

    n = defin_n(p, q)
    z = defin_z(p, q)

    lista_e = []
    for i in range(2, z):
        #print(euclides_diagram(z, i))
        if euclides_diagram(z, i):
            lista_e.append(euclides_diagram(z, i))


    for num in range((int(len(lista_e)/2)), len(lista_e)):
        e = lista_e[num]
        d = find_d(e, z)
        if d == "Não encontrado":
            continue
        else:
            break

    util.loading_spinner(1, "Buscando variante N")
    pyperclip.copy(str(n))
    print("A variante N foi copiada na sua área de transferência!")
    util.loading_spinner(1, "Buscando variante Z")
    util.loading_spinner(1, "Adquirindo variante E")
    util.loading_spinner(2, "Analisando possíveis variantes D")
    print(f'''
╔══════════════════════════════════════════════════════╗
║             RESULTADOS DA CRIPTOGRAFIA               ║
╠══════════════════════════╦═══════════════════════════╣
║  PRIMO P: {p:<14.0f} ║  PRIMO Q: {q:<15.0f} ║
║  MÓDULO N: {n:<13.0f} ║  TOTIENTE Z: {z:<12.0f} ║
╠══════════════════════════╩═══════════════════════════╣
║  EXPOENTE PÚBLICO (E): {e:<29.0f} ║
║  EXPOENTE PRIVADO (D): {d:<29.0f} ║
╚══════════════════════════════════════════════════════╝
''')
    mensagem = input("- Digite a mensagem para ser criptografada: ")

    transf1 = msg_to_ascii(mensagem)
    print("\nMensagem em Ascii:\n",transf1, "\n")
    transf2 = ascii_to_crypt(transf1, e, n)
    print("Mensagem Criptografada:\n",transf2, "\n")
    transf3 = crypt_to_ascii(transf2, d, n)
    print("Mensagem em Ascii:\n",transf3, "\n")
    transf4 = ascii_to_msg(transf3)
    print("Mensagem Normal:\n",transf4, "\n")
