# Python String strip() Método
# O que é strip()O método remove qualquer guia e espaços em branco.
texto = '     banana     '
x = texto.strip()
print('of all fruits', x, 'is my favorite')

# Remova os personagens principais:
texto2 = ',,,,,rrttgg.....banana....rrr'
x = texto2.strip(',.grt')
print(x)
