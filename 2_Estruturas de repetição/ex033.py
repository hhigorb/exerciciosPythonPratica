"""
Ordene em ordem crescente/decrescente das músicas mais tocadas.

Dica: use sorted().



lista=[
    ('Música3',{'toques':137}),
	('Música7',{'toques':2}),
	('Música11',{'toques':30}),
	('Música9',{'toques':45}),
	('Música10',{'toques':79}),
	('Música2',{'toques':190}),
	('Música8',{'toques':201}),
	('Música5',{'toques':44}),
	('Música1',{'toques':29}),
	('Música6',{'toques':14}),
	('Música4',{'toques':14}),
]
"""

lista = [
    ('Música3', {'toques': 137}),
    ('Música7', {'toques': 2}),
    ('Música11', {'toques': 30}),
    ('Música9', {'toques': 45}),
    ('Música10', {'toques': 79}),
    ('Música2', {'toques': 190}),
    ('Música8', {'toques': 201}),
    ('Música5', {'toques': 44}),
    ('Música1', {'toques': 29}),
    ('Música6', {'toques': 14}),
    ('Música4', {'toques': 14}),
]

print(sorted([toque[1]['toques'] for toque in lista]))
print(sorted([toque[1]['toques'] for toque in lista], reverse=True))

# ou

print(sorted(lista, key=lambda musica: musica[1]['toques']))
print(sorted(lista, key=lambda musica: musica[1]['toques'], reverse=True))
