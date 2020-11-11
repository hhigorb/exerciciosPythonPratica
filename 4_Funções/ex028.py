"""
Considere as variáveis

var1=['Hello World!']
var2=True and all([True or False,()])
var3=('10',) if 10>4 else 1
var4=('Hello World!')
var5=('Python is love!',)

a) Verifique e imprima o tipo destas variáveis na tela.

['Hello World!'] <class 'list'>
False <class 'bool'>
('10',) <class 'tuple'>
Hello World! <class 'str'>
('Python is love!',) <class 'tuple'>


b) Verifique se essas variáveis são objetos do tipo tupla, isto é, instâncias da classe tupla.

['Hello World!'] Não é uma tupla
False Não é uma tupla
('10',) É uma tupla!
Hello World! Não é uma tupla
('Python is love!',) É uma tupla!
"""

var1 = ['Hello World!']
var2 = True and all([True or False,()])
var3 = ('10',) if 10>4 else 1
var4 = ('Hello World!')
var5 = ('Python is love!',)

# a)

for i in var1, var2, var3, var4, var5:
    print(i, type(i))

# b)

for i in var1, var2, var3, var4, var5:
    if type(i) == tuple:
        print(f'{i} é uma tupla!')
    else:
        print(f'{i} não é uma tupla!')