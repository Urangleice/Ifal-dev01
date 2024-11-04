def main():
    nome = input("Qual seu nome?")
    ola()
    ola(nome)

def ola(para="Mundo"):
    print("Olá", para.title())

main()
