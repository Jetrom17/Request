# Para importar o método GET que está incluído, mais "json".

import requests
import json

# Para importar a cor GREEN que está incluído.

import sys

# Armazenando dados, mais API, mais "input" e obtendo dados formato "json".

req = 'https://api.invertexto.com/v1/validator?token=SEUTOKEN&value='
value = '&type=cpf'
x = input('Ponha o CPF: ')
dados = requests.get(req + x + value)
print(dados.json())


# Inserindo cor no texto.

red = '\033[31m'
print(red+"""
  _____   _   _   ___    ____   __  __      _    
 | ____| | \ | | |_ _|  / ___| |  \/  |    / \   
 |  _|   |  \| |  | |  | |  _  | |\/| |   / _ \  
 | |___  | |\  |  | |  | |_| | | |  | |  / ___ \ 
 |_____| |_| \_| |___|  \____| |_|  |_| /_/   \_\
                                                 """+red)
