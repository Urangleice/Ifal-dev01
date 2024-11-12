def main():
    #solicitar o número
    print(" --- VERIFICADOR DE PARIDADE --- ")
    num = int(input("Digite um número: "))

    #verificar se é par
    if eh_par(num): 
        print("Esse número é par")   #exibir o resultado
    else:
        print("Esse número é ímpar")

def eh_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

main()


""" O que é Snake Case?
      eh_Par           
    O que é Kebab Case?
      eh-par
    O que é Camel Case?
      EhPar()"""

