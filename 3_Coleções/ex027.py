"""
A partir das listas

linguagens=['php','JavaScript']
frases=['Eu amo ','Eu odeio ']

Use List Comprehension e obtenha a seguinte lista:

['Eu amo php !', 'Eu odeio php !', 'Eu amo JavaScript !', 'Eu odeio JavaScript !']
"""

frases = ['Eu amo ', 'Eu odeio ']
linguagens = ['PHP', 'JavaScript']

print([frase+linguagem for linguagem in linguagens for frase in frases])

