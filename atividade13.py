#Exercício Python 14: Faça um programa que leia três números e
# mostre qual é o maior e qual é o menor.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))


maior = max(num1, num2, num3)


menor = min(num1, num2, num3)

# Mostra o resultado
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")
