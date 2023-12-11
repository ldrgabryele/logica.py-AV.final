#Escreva um programa que repita a leitura de uma senha até que
#ela seja válida

#criar uma váriavel onde entre os algoritimos para a senha
senha = int(input("Digite sua senha (com até 4 digitos): "))
#crir uma condicional onde ela possa verificar a senha
#e adicionar a mensagem "Acesso Permitido" se for a senha verdadeira
#ou "Senha Invalida" se não for a senha verdadeira
if senha != 2002:
    print("Senha Invalida")
else:
    print("Acesso Permitido")