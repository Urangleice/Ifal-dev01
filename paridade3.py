def main():
    #solicitar o número
    print(" --- VERIFICADOR DE PARIDADE --- ")
    num = int(input("Digite um número: "))

    #verificar se é par
    if eh_par(num): 
        print(f"{num} é par")   #exibir o resultado
    else:
        print(f"{num} é ímpar")

def eh_par(num):
    return num % 2 == 0
    
main()
