#biblioteca de cores apenas para ilustrar melhor os erros digitados pelo usuario
from colorama import Fore, Back, Style, init
init(autoreset=True)

#Cadastrando nome do usuario
while True:
    nome = input('Nome completo: ').strip().title()
    if len(nome) <= 3:
       print(Back.RED + 'Nome invalido. Digite novamnete')

    elif not nome.replace(' ', '').isalpha(): #substiui os espaços e verifica se contem apenas letras no nome
        print('Nome inválido. Digite novamente: ')
    elif " " not in nome:  # Se não houver espaços no nome
        print("Parece que você digitou tudo junto. Digite seu nome completo corretamente: ")

    else:
        break
    
#Cadastrando idade do usuario
while True:
    try:
        idade = int(input('Idade ').strip())
        if idade < 0 or idade > 150:
            print('Idade inválida. Digite sua idade novamente:  ')        
        else:
            break
    except ValueError:
        print('Por favor insira um numero valido para a idade ')


#Cadastrando salario do usuario
while True:
    try: 
        salario = int(input('Salario (apenas numeros): ').strip())
        if salario < 0:
            print('Salario invalido. Digite um valor maior ou igual a 0.')

        else:
            break
    except ValueError:
        print('Salario invalido. Digite novamente.')

#Cadastrando sexo do usuario
while True:
    sexo = input('Sexo: Digite M para masculino ou F para feminino  ').upper().strip()
    if sexo not in 'MF':
        print('Sexo inválido! Digite M para masculino ou F para feminino')
            
    elif len(sexo) > 1:
        print('Sexo inválido! Digite M para masculino ou F para feminino')
    else:   
        break

if sexo == "M":
    sexo_formatado = "Masculino"
else:
    sexo_formatado = "Feminino"

print(f'''\nNome: {nome}
Idade: {idade}
Salário: ${salario:.2f}
Sexo: {sexo_formatado}''')