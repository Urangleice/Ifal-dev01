#ENTRADA
#Solicitar a pontuação do aluno
print("--- CONVERSÃO DE PONTOS ---")
pontos = int(input("Pontos: "))

#PROCESSAMENTO
#Verificar qual a nota aluno com base
if pontos >= 90 and pontos <= 100:
    print("Nota: A")   #SAÍDA - exibir a nota pro usuário 
elif pontos <= 80 and pontos < 90:
    print("Nota: B")
elif pontos >= 70 and pontos < 80:
    print("Nota: C")
elif pontos >= 60 and pontos < 70:
    print("Nota: D")
else:
    print("Nota: F")

