vendas = [941, 852, 783, 714, 697, 686, 685, 670, 631, 453, 386, 371, 294, 269, 259, 218, 208, 163, 125, 102, 87, 47, 7]

vendedores = ['Maria', 'José', 'Antônio', 'João', 'Francisco', 'Ana', 'Luiz', 'Paulo', 'Carlos', 'Manoel', 'Pedro', 'Francisca', 'Marcos', 'Raimundo', 'Sebastião', 'Antônia', 'Marcelo', 'Jorge', 'Márcia', 'Geraldo', 'Adriana', 'Sandra', 'Luis']
meta = 50

contador = 0
for i, venda in enumerate(vendas):
    if venda > meta:
        contador += 1
        print('{} bateu a meta. Vendas {}'.format(vendedores[i], venda))
    else:
        print('{} nao bateu a meta. Vendas: {}'.format(vendedores[i], venda))
        
print('apenas {} vendedroes bateram a meta'.format(contador))
