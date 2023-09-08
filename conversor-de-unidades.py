print("\n**********Conversor Simples de Unidades**********")
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

print("\n_____Conversão de Unidades de Temperatura_____")
print("              1-kelvin para celsius")
print("              2-kelvin para fahrenheit")
print("              3-celsius para kelvin")
print("              4-celsius para fahrenheit")
print("              5-fahrenheit para celsius")
print("              6-fahrenheit para kelvin")

convuni = input("\nDigite o número da conversão desejada: ")
n1 = float(input("Digite o valor a ser convertido: "))
if "1" in convuni:
    print(kelforcel(n1))
elif "2" in convuni:
    print(kelforfah(n1))
elif "3" in convuni:
    print(celforkel(n1))
elif "4" in convuni:
    print(celforfah(n1))
elif "5" in convuni:
    print(fahforcel(n1))
elif "6" in convuni:
    print(fahforkel(n1))




    



