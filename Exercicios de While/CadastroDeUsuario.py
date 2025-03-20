#Pegando nome do usuario
nome = input('Nome completo: ').strip().title()
while True:
    if len(nome) <= 3:
        print('Nome inválido. Digite seu nome novamente: ')
        continue
    elif not nome.replace(' ', '').isalpha(): #substiui os espaços e verifica se contem apenas letras no nome
        print('Nome inválido. Digite seu nome novamente: ')
        continue
    elif " " not in nome:  # Se não houver espaços no nome
        print("Parece que você digitou tudo junto. Digite seu nome completo corretamente: ")
        continue

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