#criar uma variavel para o valor do salario
salario = float(input("Digite o valor do salário: "))
#criar uma condicional já que as porcentagens são diferentes
#ajustar o print para que o exibir o valor do novo salario, do 
#reajuste de ganho e a porcentagem
if salario >=0 and salario <= 400.01:
    print(f"""
    Novo salario: {(salario) + salario*15/100:.2f}
    Reajuste ganho: {salario*15/100:.2f} 
    Em percentual: 15%""")

elif salario >=400.01 and salario <= 800.00:
    print(f"""
    Novo salario: {(salario) + salario*12/100:.2f}
    Reajuste ganho: {salario*12/100:.2f} 
    Em percentual: 12%""")

elif salario >= 800.01 and salario <= 1200.00:
    print(f"""
    Novo salario: {(salario) + salario*10/100:.2f}
    Reajuste ganho: {salario*10/100:.2f} 
    Em percentual: 10%""")

elif salario >= 1200.01 and salario <= 2000.00:
    print(f"""
    Novo salario: {(salario) + salario*7/100:.2f}
    Reajuste ganho: {salario*7/100:.2f} 
    Em percentual: 7%""")

else:
    print(f"""
    Novo salario: {(salario) + salario*7/100:.2f}
    Reajuste ganho: {salario*4/100:.2f}
    Em percentual: 4%""")
    