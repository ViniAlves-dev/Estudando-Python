nome = input('Nome ').strip().capitalize()
while True:
    if len(nome) <= 3:
        nome = input('Nome inválido. Digite seu nome novamente: ').strip().capitalize().isalpha()
    elif not nome.replace(' ', '').isalpha():
        nome = input('Nome inválido. Digite seu nome novamente: ').strip().capitalize().isalpha()
    else:
        nome = nome.title()
        break
    

while True:
    try:
        idade = int(input('Idade '))
        if idade < 0 or idade > 150:
            idade = int(input('Idade inválida. Digite sua idade novamente:  '))
        else:
            break
    except ValueError:
        print('Por favor insira um nuemero valido para a idade ')

print('''\nNome: {}
Idade: {}'''.format(nome, idade))