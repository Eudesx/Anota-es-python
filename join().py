# Python String join() Method
# Junte todos os itens em uma tupla em uma string, usando um caractere hash como separador:
# Uma cadeia deve ser especificada como o separador.
mytuple = ('manga', 'banana', 'abacaxi')
x = '#'.join(mytuple)
print(x)

# Junte todos os itens em um dicionário em uma string, usando a palavra "TEST" como separador:
mydict = {'name': 'Jonh', 'Country': 'Jorway'}
myseparator = 'TEST'
x2 = myseparator.join(mydict)
print(x2)

