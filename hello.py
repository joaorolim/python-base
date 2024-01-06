#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente, o programa exibe a mensagem
correspondente.

Como usar:
Tenha a variável LANG devidamente configurada. Ex:
    export LANG=pt_BR.utf8

Execução:
    python3 hello.py
    ou
    ./hello.py
""" 

# metadadados
__version__ = "0.1.2"
__author__ = "João Paulo Rolim"
__license__ = "Unlicense" 

import os

os_lang = os.getenv("LANG", "en_US.utf8")  # 'C.UTF-8'
current_language = os_lang.split(".")[0]
current_encoding = os_lang.split(".")[1]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
    "C": "Olá, Mundo !!!",
}

# Busca O(1) - constante por causa da Hash Table
print(msg[current_language])

# export LANG=it_IT.utf8 
# export LANG=C.UTF-8 
