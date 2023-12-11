#Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos.
#Na proxima linha, deve-se mostrar a média de todos os valores positivos digitados,
#com um digito após o número decimal

#criar duas variaveis zeradas
positivos = 0
soma = 0
#criar um loop para que percorra cada valor e o verifique
for valores in range(1,7):
    valor = float(input(f"Digite o {valores} valor: "))
    if valor > 0:
        positivos +=1
        soma += valor
#fazer a formula da média e exibir os resultados 
media = soma/positivos
print(f"{positivos} valores positivos")
print(f"{round(media,2)}")