"""
Escreva um programa que replique o padrão de caracteres descrito a seguir.

Dica: use loop for.

*
**
***
****
*****
*****
******
*******
********
*********
**********
*********
********
*******
******
*****
****
***
**
*
"""

for i in range(1, 10):
    print('*' * i)
for i in range(10, 1, -1):
    print('*' * i)
