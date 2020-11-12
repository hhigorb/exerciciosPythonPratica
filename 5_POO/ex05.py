"""
Crie uma classe Lampada com os seguintes atributos e métodos:

Atributos:

Cor;

Voltagem;

Luminosidade;

Ligada (a lâmpada deve inicializar desligada).

Métodos:

Verificar se a lâmpada está ligada/desligada

Ligar/desligar a lâmpada.

Todos os atributos devem ser privados.

Crie um objeto da classe Lampada e teste os métodos criados.
"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        if self.__ligada:
            return 'A lâmpada está ligada'
        return 'A lâmpada está desligada'

    def liga_desliga(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


lampada1 = Lampada('Branca', '110V', 80)
print(lampada1.checa_lampada())
lampada1.liga_desliga()
print(lampada1.checa_lampada())
lampada1.liga_desliga()
print(lampada1.checa_lampada())