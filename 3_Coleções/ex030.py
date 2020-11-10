"""
A partir da lista

frutas=['  BaNanA    ', '  morangO ', ' mAçã  ','   MeLão']

Use List Comprehension e obtenha as seguintes listas:

['Eu gosto de Banana !', 'Eu gosto de Morango !', 'Eu gosto de Maçã !', 'Eu gosto de Melão !']
['BANANA', 'MORANGO', 'MAÇÃ', 'MELÃO']
['banana', 'morango', 'maçã', 'melão']
"""

frutas = ['  BaNanA    ', '  morangO ', ' mAçã  ', '   MeLão']

print(['Eu gosto de ' + fruta.strip().title() for fruta in frutas])
print([fruta.upper().strip() for fruta in frutas])
print([fruta.lower().strip() for fruta in frutas])
