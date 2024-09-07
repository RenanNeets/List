#Dictionary Comprehension
produto = {
    'nome':'Cante Azul',
    'preco':2.3,
    'categoria':'Escritório'
}
dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave,valor
    in produto.items()
    if chave !='categoria'
}
print(dc)

#Set comprehension
s1 = {i *2 for i in range(10)}
print(s1)