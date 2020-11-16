"""
Crie uma classe Cliente com os seguintes atributos e métodos:

Atributos (todos privados):

Nome;

E-mail;

Telefone;

Senha.



Métodos:

Mostrar nome;

Mostrar sobrenome;

Mostrar e-mail;

Mostrar telefone;

Alterar nome *;

Alterar Senha *;

Resumo (mostra todas as informações do cliente, inclusive a senha).

*Para alterar essas informações, peça a senha do usuário, e caso a senha seja correta permita a modificação.



Crie um objeto para testar os métodos e atributos da classe Cliente.
"""


class Cliente:
    def __init__(self, nome, email, telefone, senha):
        self.__nome = nome
        self.__email = email
        self.__telefone = telefone
        self.__senha = senha

    @property
    def mostrar_nome(self):
        return f'Seu nome é: {self.__nome}'

    @property
    def mostrar_email(self):
        return f'Seu sobrenome é: {self.__email}'

    @property
    def mostrar_telefone(self):
        return f'Seu telefone é: {self.__telefone}'

    @mostrar_nome.setter
    def mostrar_nome(self, novo_nome):
        senha = int(input('Digite sua senha para alterar seu nome: '))
        if self.__senha == senha:
            self.__nome = novo_nome
            print('Nome alterado com sucesso!')
        else:
            print(f'Senha incorreta!')

    def alterar_senha(self, nova_senha):
        senha = int(input('Digite sua senha para alterar sua senha: '))
        if senha == self.__senha:
            self.__senha = nova_senha
            print('Senha alterada com sucesso!')
        else:
            print(f'Senha incorreta!')

    def resumo(self):
        return self.__dict__


# instanciando objeto do tipo Cliente:

cliente1 = Cliente('Higor', 'hhigorb@outlook.com', 'xxxxxxxxxxxx', 12345)

# testando os métodos da classe Cliente:

print(cliente1.mostrar_nome)
print(cliente1.mostrar_email)
print(cliente1.mostrar_telefone)
print(cliente1.resumo())

# testando os Setters:

cliente1.mostrar_nome = 'Rogério'
cliente1.alterar_senha(54321)
print(cliente1.resumo())

