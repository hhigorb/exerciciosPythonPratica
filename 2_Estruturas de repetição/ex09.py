"""
Em um único loop escreva um programa que mostre na tela de 1 a 10 três vezes e ao final mostre a mensagem Fim.
No primeiro loop utilize for e nos dois loops seguintes while. O resultado do seu programa deverá ter o seguinte
formato:

1
2
3
4
5
6
7
8
9
10
1
2
3
4
5
6
7
8
9
10
1
2
3
4
5
6
7
8
9
10
Fim
"""

for i in range(3):
    n = 1
    while n <= 10:
        print(n)
        n += 1
print('Fim')


