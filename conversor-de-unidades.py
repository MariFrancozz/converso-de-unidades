print("\n**********Conversor Simples de Unidades**********")

#Definição de funções
def kelforcel (n1):
    resul = n1 - 263
    print("O resultado da conversão de kelvin para celsius é: ", resul)
def kelforfah (n1):
    resul = (n1 - 273) * 1.8 + 32
    print("O resultado da conversão de kelvin para fahrenheit é: ", resul)
def celforkel (n1):
    resul = n1 + 273
    print("O resultado da conversão de celsius para kelvin é: ", resul)
def celforfah (n1):
    resul = n1 * 1.8 + 32
    print("O resultado da conversão de celsius para fahrenheit é: ", resul)
def fahforcel (n1):
    resul = (n1 - 32) / 1.8
    print("O resultado da conversão de fahrenheit para celsius é: ", resul)
def fahforkel (n1):
    resul = (n1 - 32) * 5 / 9 + 273
    print("O resultado da conversão de fahrenheit para kelvin é: ", resul)

#Tabela com as conversões possíveis
def conversoes(y):
    print("\n_____Conversão de Unidades de Temperatura_____")
    print("              1-kelvin para celsius")
    print("              2-kelvin para fahrenheit")
    print("              3-celsius para kelvin")
    print("              4-celsius para fahrenheit")
    print("              5-fahrenheit para celsius")
    print("              6-fahrenheit para kelvin")

#Realizando a conversão
convuni = int(input("\nDigite o número da conversão desejada: "))
n1 = float(input("Digite o valor a ser convertido:  "))
if convuni == 1:
    print(kelforcel(n1))
elif convuni == 2:
    print(kelforfah(n1))
elif convuni == 3:
    print(celforkel(n1))
elif convuni == 4:
    print(celforfah(n1))
elif convuni == 5:
    print(fahforcel(n1))
elif convuni == 6:
    print(fahforkel(n1))

#Tentativa de prevenção de erro caso a pessoa não selecione algumas das conversões possíveis 
else:
    print("Você não selecionou uma das opções válidas.")
    escolha = input("Digite y para tentar novamente ou n para sair do conversor: ")
    if escolha == "y":
        print(conversoes(2))
        convuni = int(input("\nDigite o número da conversão desejada: "))
        n1 = float(input("Digite o valor a ser convertido:  "))
        if convuni == 1:
            print(kelforcel(n1))
        elif convuni == 2:
            print(kelforfah(n1))
        elif convuni == 3:
            print(celforkel(n1))
        elif convuni == 4:
            print(celforfah(n1))
        elif convuni == 5:
            print(fahforcel(n1))
        elif convuni == 6:
            print(fahforkel(n1))
        else:
            print("Você saiu do conversor")
                
          