Este é um tutorial simples usando método do tipo **GET**, mais API de Invertexto.

Segue o código em python:

```
# Para importar o método GET que está incluído.

import requests

# Para importar a cor GREEN que está incluído.

import sys

# Armazenando dados, mais API, mais "input" e obtendo dados formato "json".

req = 'https://api.invertexto.com/v1/validator?token=SEUTOKEN&value=NÚMERO'
value = '&type=cpf'
x = input('Ponha o CPF: ')
dados = requests.get(req + x + value)
print(dados.json())

# Inserindo cor no texto.

color = '\033[31m'
print(green+"""
      _          _                              
     | |   ___  | |_   _ __    ___    _ __ ___  
  _  | |  / _ \ | __| | '__|  / _ \  | '_ ` _ \ 
 | |_| | |  __/ | |_  | |    | (_) | | | | | | |
  \___/   \___|  \__| |_|     \___/  |_| |_| |_|
                                                """+green)
```

Após executar em um ambiente python, coloque o cpf desejado e terás a informação sobre o CPF, sendo **verdadeiro** ou **falso**.

# Como faço para obter o TOKEN?

Boa pergunta, você deve se registrar na plataforma [Invertexto](https://api.invertexto.com/register). Depois **crie seu token**, em sequida é gerado automaticamente um. Após isto, substitua no código a cima na variável **req** especificamente na url em, **SEUTOKEN** pelo seu token criado.


[Tabnews](https://github.com/Jetrom17/Request](https://www.tabnews.com.br/Jetrom/python-validador-de-cpf).
