"""
Em um único loop escreva um programa que mostre na tela de 0-5, cinco vezes e ao final mostre a mensagem Fim.
Utilize apenas for em sua implementação. Seu programa deverá gerar um output com o seguinte formato:

0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
0
1
2
3
4
5
Fim
"""

for i in range(5):
    for j in range(0, 6):
        print(j)
print('Fim')

