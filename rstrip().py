# Python String rstrip() Method
# Remova quaisquer espaços em branco no final da cadeia de caracteres(Começando pela direita)
texto = '     banana     '
x = texto.rstrip()
print('of all fruits', x, 'is my favorite')

# Remova os caracteres de arrasto se forem vírgulas, pontos, pontos, s, q ou w:
texto2 = 'banana,,,,,ssqqqww....'
x = texto2.rstrip(',.qsw')
print(x)
