#List comprehension é uma forma rápida para criar listas
#a partir de iteráveis


#print(list(range(10)))
# OU
lista = []
for numero in range(10):
    lista.append(numero)
#print(lista)

# OU
#List compreh.
#lista=[numero for numero in range(10)]

#list compreh. modif
lista=[
    numero *2
    for numero in range(11)
]
#print(lista)
produtos = [
    {'nome':'p1','preco':20,},
    {'nome':'p2','preco':10,},
    {'nome':'p3','preco':30,},
]
novos_produtos = [
    #['nome':produto['nome'], 'preco': produto['preco']]
    {**produto, 'preco':produto['preco']*1.05}
    if produto['preco']>20 else {**produto}
    for produto in produtos
]
#print(*novos_produtos, sep='\n')

#------- FILTER ---
import pprint
def p(v):
    pprint.pprint(v, sort_dicts =False, width=40)
#p(novos_produtos)
lista = [
    #n for n in range(10) if n <5
    {**produto, 'preco':produto['preco']*1.05}
    if produto['preco']>20 else {**produto}
    for produto in produtos
    if produto['preco']>10
]
#print(lista)
""""
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))
"""
# OU
lista = [
    (x,y)
    for x in range(3)
    for y in range(3)
]
# OU
lista = [
    [x for y in range(3)]
    for x in range(3)
]
print(lista)
