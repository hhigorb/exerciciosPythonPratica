"""
Use list() e zip() para criar uma nova lista de tuplas com as listas a seguir.

paises=['Brasil','Brasil','Brasil','EUA','EUA','EUA','EUA']
estados=['São Paulo','Bahia','Rio de Janeiro','Alabama','Alabama','Alabama','Califórnia']
cidades=['São Paulo','Salvador','Rio de Janeiro','Birmingham','Huntsville','Mobile','Beverly Hills']

output:

[('Brasil', 'São Paulo', 'São Paulo'), ('Brasil', 'Bahia', 'Salvador'), ('Brasil', 'Rio de Janeiro', 'Rio de Janeiro'),
('EUA', 'Alabama', 'Birmingham'), ('EUA', 'Alabama', 'Huntsville'), ('EUA', 'Alabama', 'Mobile'),
('EUA', 'Califórnia', 'Beverly Hills')]

"""

paises = ['Brasil', 'Brasil', 'Brasil', 'EUA', 'EUA', 'EUA', 'EUA']
estados = ['São Paulo', 'Bahia', 'Rio de Janeiro', 'Alabama', 'Alabama', 'Alabama', 'Califórnia']
cidades = ['São Paulo', 'Salvador', 'Rio de Janeiro', 'Birmingham', 'Huntsville', 'Mobile', 'Beverly Hills']

print(list(zip(paises, estados, cidades)))

