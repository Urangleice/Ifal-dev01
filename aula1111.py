print("--- O QUANTO VOCÊ VAI VIVER? ---")
print(" -> baseado no tipo de comida que você consome")

x = int(input("De 1 a 10, quanto você come comida saudável? "))
y = int(input("De 1 a 10, quanto você come porcaria? "))

if x or y > 10 or x or y < 1:
    print("Eu disse de 1 a 10...")
else:
    if x < y:
        print("Dos 25 você não passa.")
    elif x > y:
        print("Continue assim e você terá uma vida longa.")
        if x == 10:
            print("a causa da sua morte com certeza não será má alimentação, parabéns!")
    else:
        print("Provavelmente vai viver até os 40/50.")
