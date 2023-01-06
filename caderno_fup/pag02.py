# Lista de Atividades

# Questão 01

numero = input("Digite um inteiro positivo: ")

valor = int(numero)

numero_sem_zeros_a_esquerda = str(valor)

espelho = numero_sem_zeros_a_esquerda[::-1]

print(f"Número espelhado: {espelho}.")

# Questão 02

valor_espelhado = int(espelho)

comparacao = "igual a"
if valor < valor_espelhado:
    comparacao = "menor que"
elif valor > valor_espelhado:
    comparacao = "maior que"
    
print(f"{valor} é {comparacao} {valor_espelhado}")

# Questão 03

palavra = input("Digite uma palavra de 5 letras: ")

if palavra[0] == palavra[4] and palavra[1] == palavra[3]:
    print("É palíndromo.")
else:
    print("Não é palíndromo.")

inverso = palava[::-1]

if palavra == inverso:
    print("É palíndromo.")
else:
    print("Não é palíndromo.")
    
# Questão 04

numero = input("Digite um número inteiro positivo: ")
numero = int(numero)

if numero % 2 == 0:
    print("É divisível por 2.")
else:
    print("Não é divisível por 2.")

if numero % 35 == 0:
    print("É divisível por 5.")
    print("É divisível por 7.")
    if numero % 10 == 0:
        print("É divisível por 10.")
    else:
        print("Não é divisível por 10.")
    print("É divisível por 35.")
elif numero % 10 == 0:
    print("É divisível por 5.")
    if numero % 7 == 0:
        print("É divisível por 7.")
    else:
        print("Não é divisível por 7.")
    print("É divisível por 10.")
    print("Não é divisível por 35.")
elif numero % 7 == 0:
    if numero % 5 == 0:
        print("É divisível por 5.")
    else:
        print("Não é divisível por 5.")
    print("É divisível por 7.")
    print("Não é divisível por 10.")
    print("Não é divisível por 35.")
elif numero % 5 == 0:
    print("É divisível por 5.")

    print("Não é divisível por 7.")
    print("Não é divisível por 10.")
    print("Não é divisível por 35.")
else:
    print("Não é divisível por 5.")
    print("Não é divisível por 7.")
    print("Não é divisível por 10.")
    print("Não é divisível por 35.")
