#Pegando nome do usuario
while True:
    nome = input('Nome completo: ').strip().title()
    if len(nome) <= 3:
       print('Nome invalido. Digite novamnete')

    elif not nome.replace(' ', '').isalpha(): #substiui os espaços e verifica se contem apenas letras no nome
        print('Nome inválido. Digite novamente: ')
    elif " " not in nome:  # Se não houver espaços no nome
        print("Parece que você digitou tudo junto. Digite seu nome completo corretamente: ")

    else:
        break
    
#Pegando idade do usuario
while True:
    try:
        idade = int(input('Idade ').strip())
        if idade < 0 or idade > 150:
            print('Idade inválida. Digite sua idade novamente:  ')        
        else:
            break
    except ValueError:
        print('Por favor insira um numero valido para a idade ')


#Pegando salario do usuario

salario = input('Salario').strip()





print('''\nNome: {}
Idade: {}'''.format(nome, idade))