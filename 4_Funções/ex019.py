"""
Considere a lista nomes a seguir e responda:

nomes=['','Roberto Carlos','Tom Jobim','Jorge Amado','Machado de Assis','Zé Ramalho','Elba Ramalho','','',[],()]

a) obtenha uma nova lista sem os objetos vazios.

output:

['Roberto Carlos', 'Tom Jobim', 'Jorge Amado', 'Machado de Assis', 'Zé Ramalho', 'Elba Ramalho']

b) obtenha uma nova lista que tenha apenas os nomes com o sobrenome Ramalho.

output:

['Zé Ramalho', 'Elba Ramalho']
"""

nomes = ['', 'Roberto Carlos', 'Tom Jobim', 'Jorge Amado', 'Machado de Assis', 'Zé Ramalho', 'Elba Ramalho',
         '', '', [], ()]

# a)

print(list(filter(lambda valor: len(valor) > 0, nomes)))

# b)

print(list(filter(lambda sobrenome: len(sobrenome) > 0 and sobrenome.split()[-1] == 'Ramalho', nomes)))

