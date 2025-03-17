#### 1. Faça um Programa que leia as vendas dos vendedores, mostre a venda de cada vendedor com o seu nome e a média de vendas. 

vendas = [1000, 1500, 1200, 1300]
vendedores = ["Fulano", "Beltrano", "Ciclano", "Lira"]

for i, venda in enumerate(vendas):
    print("{} vendeu {} produtos".format(vendedores[i], venda))

media = sum(vendas) / len(vendas)

print('Média: ', media)


#### 2. Faça um Programa que crie uma lista com as médias de cada aluno, imprima as médias de cada aluno e a quantidade de alunos com média maior que 7.

alunos = ["José", "Joana", "Maria", "Carla", "Mauricio", "Andre", "Tiago", "Enzo", "Amanda", "Alessandra"]
notas = [
    [10, 9, 8, 8],
    [9, 7, 6, 4],
    [10, 10, 10, 10],
    [5, 3, 10, 9],
    [7, 6, 6, 6],
    [7, 7, 8, 7],
    [7, 7, 7, 9],
    [8, 5, 6, 7],
    [10, 9, 7, 4],
    [10, 1, 3, 3],
]

quant_alunos_acima = 0

for i, aluno in enumerate(alunos):
    media_nota = sum(notas[i]) / 4
    print('O aluno {} ficou a média {}'.format(aluno, media_nota))
    if media_nota >= 7:
        quant_alunos_acima += 1

print('\n')
print('{} alunos ficaram com a nota acima ou igual a 7'.format(quant_alunos_acima))
print('\n')
#### 3. Foram anotadas as idades e salários de 30 funcionários. Faça um programa que determine quantos funcionários com mais de 25 anos possuem salário inferior à média de todos os salários.

idades = [35,32,50,33,48,50,33,48,22,49,35,38,20,47,49,48,34,21,48,44,48,30,25,42,42,23,25,23,38,35]
salarios = [3739,2219,3554,3978,4014,3270,4792,3879,2981,2384,4826,2460,3680,4318,1872,1770,4640,3929,3295,1729,3965,4267,4007,1916,2987,2943,3852,4543,2055,1730]

contador = 0
media_salario = sum(salarios) / len(salarios)

for i, idade in enumerate(idades):
    if idade > 25 and salarios[i] <= media_salario:
        contador += 1













