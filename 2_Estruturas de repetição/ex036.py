"""
Utilize for para obter a inversão de uma cadeia de string. Exemplos:

!
d
l
r
o
W

o
l
l
e
H



!dlroW olleH
"""

string = input('Digite uma string: ')

for letra in string[::-1]:
    print(letra)

print(string[::-1])