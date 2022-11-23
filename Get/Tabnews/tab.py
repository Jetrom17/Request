# Importe as bibliotecas:
import requests
import json
import sys
# Filtrando apenas post de Filipedeschamps!
req = requests.get("https://www.tabnews.com.br/api/v1/contents/filipedeschamps")
# Obtendo status:
print(req)
# Obtendo os dados em formato 'json':
print(req.json())
# Cor da letra em vermelho, mais exibição do texto:
""
red = '\033[31m'
print(red+"""
_________ _______ _________ _______  _______  _______ 
\__    _/(  ____ \\__   __/(  ____ )(  ___  )(       )
   )  (  | (    \/   ) (   | (    )|| (   ) || () () |
   |  |  | (__       | |   | (____)|| |   | || || || |
   |  |  |  __)      | |   |     __)| |   | || |(_)| |
   |  |  | (         | |   | (\ (   | |   | || |   | |
|\_)  )  | (____/\   | |   | ) \ \__| (___) || )   ( |
(____/   (_______/   )_(   |/   \__/(_______)|/     \|
                                                      
"""+red)

'''
Caso queira filtrar outras coisas, basta substituir a url: /api/v1/contents/{user}
ou deixe vazio para obter dados recentes da página inicial. Queira contribuir em:
https://github.com/Jetrom17/Request/Get/Tabnews

Para bom funcionamento da ferramenta em terminais baseado em Linux, consulte:
https://github.com/Jetrom17/Request
'''
