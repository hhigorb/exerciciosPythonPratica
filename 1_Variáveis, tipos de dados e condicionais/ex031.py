"""
Utilize o módulo datetime e mostre na tela a data e hora atual do sistema de acordo com o formato descrito abaixo.



12/06/2020 - 14:34:17
"""

from datetime import datetime

x = datetime.now()
print(x.strftime('%d/%m/%Y - %H:%M:%S'))




