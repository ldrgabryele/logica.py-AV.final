#Faça um programa que leia 5 valores inteiros.
#Conte quantos destes valores digitados são pares e mostre esta informação

#criar duas variaveis uma com uma lista aberta e uma zerada
valores = []
pares = 0
#criar um loop para que cada valor seja verificado
for numeros in range(1,6):
    valor = int(input(f"Digite o {numeros} valor: "))
    valores.append(numeros)
    if valor % 2 == 0:
        pares += 1
print (f"{pares} valores pares")
