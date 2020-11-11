"""
Considere a lista a seguir, com pares respectivos as capitais brasileiras e as temperaturas registradas para
um determinado dia em 2020.

Use a função map() para converter as temperaturas de °C para K e F.

temperatura_capitais_brasil=[

    ('Boa Vista',32.4),

    ('Brasília',26.6),

    ('Campo Grande',28.8),

    ('Cuiabá',38.6),

    ('Salvador',37.1),

    ('São Paulo',38.8),

    ('Rio de Janeiro',34.7)

]
"""

temperatura_capitais_brasil = [

    ('Boa Vista', 32.4),

    ('Brasília', 26.6),

    ('Campo Grande', 28.8),

    ('Cuiabá', 38.6),

    ('Salvador', 37.1),

    ('São Paulo', 38.8),

    ('Rio de Janeiro', 34.7)

]

c_para_f = map(lambda par: (par[0], round(par[1]*(9/5)+32, 1)), temperatura_capitais_brasil)
c_para_k = map(lambda par: (par[0], round(par[1]+273)) ,temperatura_capitais_brasil)

print(list(c_para_f))
print(list(c_para_k))
