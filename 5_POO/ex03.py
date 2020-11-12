"""
Crie uma classe Pessoa com as seguintes características:

Atributos:

Nome (atributo público);

E-mail (atributo público);

Senha (atributo privado).

Métodos:

Mostrar nome;

Mostrar E-mail;

Mostrar senha.



Crie um objeto da classe Pessoa para testar suas propriedades e métodos.
"""


class Pessoa:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.__senha = senha

    def mostra_nome(self):
        return f'Seu nome é: {self.nome}'

    def mostra_email(self):
        return f'Seu email é: {self.email}'

    def mostra_senha(self):
        return f'Sua senha é: {self.__senha}'


pessoa1 = Pessoa('Higor', 'teste@gmail.com', 14241499)
print(pessoa1.mostra_nome())
print(pessoa1.mostra_email())
print(pessoa1.mostra_senha())