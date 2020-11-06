"""
O Índice de Massa Corporal (IMC) é utilizado para mensurar o peso ideal de uma pessoa. Escreva um programa que
peça o nome, a idade , o peso e a altura do usuário. Ao final calcule e mostre o resultado do seu IMC e
classifique este resultado de acordo com a regra a seguir.



IMC<17 - Muito abaixo do peso ideal

17<=IMC<18,5 - Abaixo do peso

18,5<=IMC<25 - Peso normal

25<=IMC<30 - Acima do peso

30<=IMC<35 - Obesidade I

35<=IMC<40 - Obesidade II (severa)

IMC>=40 - Obesidade III (mórbida)



Lembre que: IMC=massa/(altura*altura)



Fonte: https://pt.wikipedia.org/wiki/%C3%8Dndice_de_massa_corporal
"""

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / altura ** 2

if imc < 17:
    print('Muito abaixo do peso.')
elif 17 <= imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Peso normal.')
elif 25 <= imc < 30:
    print('Acima do peso.')
elif 30 <= imc < 35:
    print('Obesidade Grau I.')
elif 35 <= imc < 40:
    print('Obesidade Grau II (severa).')
else:
    print('Obesidade Grau III (mórbida).')