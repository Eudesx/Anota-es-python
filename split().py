# Python String split() Method
# Divida uma string em uma lista onde cada palavra é um item de lista:
# O que é split()O método divide uma string em um Lista.
# Você pode especificar o separador, o separador padrão é qualquer espaço em branco.
texto = 'welcome to the jungle'
x = texto.split()
print(x)

# Divida, usando vírgula, seguida de um espaço, como um separador:
texto2 = 'hello, my name is peter, I am 26 years old'
x2 = texto2.split(', ')
print(x2)

# Use um personagem de hash como um separador:
# definir o parâmetro split como 1 retornará uma lista com 2 elementos!
texto3 = 'apple#banana#cherry#orange'
x3 = texto3.split('#', 1)
print(x3)

