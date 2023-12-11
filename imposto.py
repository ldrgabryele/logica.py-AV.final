#leia um valor com duas casas decimais, equivalente ao salário de uma pessoa
#de Lisarb. Em seguida, calcule e mostre o valor que esta pessoa deve pagar
#de imposto de renda, segundo a tabela.

#criar uma variavel para o valor do salario
salario = float(input("Digite o valor do salário: "))
#criar uma condicional já que as porcentagens são diferentes
#e exibir vamor da condiciona
if salario <= 2000.00:
    print("inseto")

elif salario >= 2000.01:
    print(f"R$ {(salario*8/100)}")

elif salario >= 3000.01:
    print(f"R$ {(salario*18/100)}")

else:
    print(f"R$ {(salario*28/100)}")


    