# Importando a biblioteca.
import requests
# Importando biblioteca de cores.
import sys
# Insira quaisquer url que suporte "json".
req = requests.get("http://ip-api.com/json/")
# Obtendo o tipo de resposta.
print(req)
# Obtendo informações do tipo "json".
print(req.json())
red = '\033[31m'
print(red+"""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:::::::::::::::::::::::::::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@::::::::::::::::::::::::::::::::::::::::::::::::::::::::: @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@!:::::::::::::::::::::::#################!::::::::::::::::::::::!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@:::::::::::::::::::::::###################!::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::#########################################################!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::###########!!!!!#########################!!!!!###########!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::##########!!###!:!!!!###############!!!!!!###!!##########!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::##########!!!!!!!####!!##!!!!!!!##!!####!!!!!!!##########!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::######################:!#!!###!!##:!#####################!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::######################:!##!!!!!###:!#####################!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::######################:!##########:!#####################!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::#######!!!!!!###########!!::::::!##!########!!!!!!#######!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::#######:!###!:########!:::!####!::!!#######!:####:!######!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::########!!:!!########!::!########::!########!!:!!!#######!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::#########!:##########!::!########::!!#########:!#########!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::##########!!!######!!:::::::::::::::!!######!!!##########!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::##############!!!##:::::::::::::::::::!#!!!!#############!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::#######!!!#!!!#####:::::::!###!:::::::!#####!!##!!#######!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::#######!!###!!!!!!#::::::::###!:::::::!#!!!!!####!!######!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::########!!:!#######::::::::!##!:::::::!######!:!!########!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::###########!!!!!!!#:::::::::::::::::::!#!!!!!!###########!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::#########!!###################################!!#########!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::#########!:!##########:!####!!####:!##########:!#########!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::#######!!##!!!########:!####!!####:!#######!!!##!!!######!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::#######!!###!!########:!####!!####:!#######!!####!!######!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::########!!!!##########:!###!!!####:!#########!!!!########!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::######################:!#!!###!!##:!#####################!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::###########!!!!!#####!!!#!!###!!##!!#####!!!!!###########!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::##########!!###!!!!!!!#############!!!!!!!###!!##########!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::##########!!!#!!!#######################!!!#!!!##########!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::#########################################################!:::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@:::::::::::::::::::::::::::::::!!!:::::::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@:::::::::::::::::::::::::::::#######:::::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@::::::::::::::::::::::::::::!########::::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@!::::::::::::::::::::::::::::!#####!::::::::::::::::::::::::::::!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@!:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::!@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@::::::::::::::::::::::::::::::::::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!:::::::::::::::::::::::::::::::::::::::::::::::::::::@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""+red)

# Se executado como está, terás informações sobre si.

# {
#    "status": " ",
#    "country": " ",
#    "countryCode": " ",
#    "region": " ",
#    "regionName": " ",
#    "city": " ",
#    "zip": " ",
#    "lat": -0.000,
#    "lon": -00.0000,
#    "timezone": " ",
#    "isp": " ",
#    "org": " ",
#    "as": " ",
#    "query": " "
# }

# Leia a documentação completa em: https://ip-api.com/docs/api:json
