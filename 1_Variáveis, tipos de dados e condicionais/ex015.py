"""
Elabore um programa para calcular a hipotenusa de um triângulo.

Dicas:

Veja o módulo math (math.hypot);

Utilize a seguinte fórmula: hipotenusa=(a²+b²)¹/2:
"""

catetoa = float(input('Digite o cateto adjacente: '))
catetoo = float(input('Digite o cateto oposto: '))
hipotenusa = (catetoa ** 2 + catetoo ** 2) ** (1/2)

print(f'Hipotenusa: {hipotenusa:.2f}')