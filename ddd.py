#Leia um número inteiro que representa um código de DDD para
#discagem interurbana. Em seguida, informe á qual cidade o DDD
#pertence, considerando a tabela da atividade

#criar variavel para receber o valor do DDD
DDD = int(input("Digite o seu DDD: "))
#criar condicinal para cada DDD da tabela de acordo com a sua 
#cidade, se for diferente dos da tabela adicionar a mensagem
# "DDD não cadastrado"
if DDD == 61:
    print("Brasilia")
elif DDD == 71:
    print("Salvador")
elif DDD == 11:
    print("São Paulo")
elif DDD == 21:
    print("Rio de Janeiro")
elif DDD == 32:
    print("Juiz de Fora")
elif DDD == 19:
    print("Campinas")
elif DDD == 27:
    print ("Vitoria")
elif DDD == 31:
    print ("Belo Horizonte")
else:
    print("DDD não cadastrado")