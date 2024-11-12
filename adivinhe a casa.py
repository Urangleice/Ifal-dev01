"""PROGRAMA/JOGO AINDA NÃO ACABADO"""

#informar a casa do personagem de Harry Potter
print(" --- Adivinhe a casa do personagem --- ")

def botao_simulado():
    print("Pressione 'E' para continuar ou 'F' para ver lista de personagens")
    
    while True:
        comando = input("Digite sua opção: ")
        
        if comando.upper() == 'E':
            print("Botão pressionado!")
            break  # Encerra o loop após pressionar o botão.
        elif comando.upper() == 'F':
            print("Saindo...")
            break  # Encerra o loop caso o usuário queira sair.
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função para "simular" o botão
botao_simulado()



#verificar qual a casa deste personagem
"""
Harry: Grifinória
Hermione: Grifinória
Rony: Grifinória
Draco: Sonserina
Luna: Corvinal
Cedric: Lufa-lufa
outra opção: personagem não encontrado
"""

#informar ao usuário qual a casa do personagem