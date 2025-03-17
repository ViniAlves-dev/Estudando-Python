# Calcular a porcentagem de 30% dos vendedores que bateram a meta a partir de uma lista de vendas.

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

bateram_meta = []
for venda in vendas:
    if venda[1] >= meta:
        bateram_meta.append(venda[1])
print('apenas {:.1%} dos vendedores bateram a meta'.format(len(bateram_meta) / len(vendas)))



#Definindo quem foi o vendedor que mais vendeu 

melhor_vendedor = ''
maior_venda = 0
for venda in vendas:
    if venda[1] >= maior_venda:
        maior_venda = venda[1]
        melhor_vendedor = venda[0]
print('sendo {} a vendedorora que mais vendeu, com o total de {} vendas'.format(melhor_vendedor, maior_venda))