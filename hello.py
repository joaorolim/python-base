#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente, o programa exibe a mensagem
correspondente.

Como usar:
Tenha a variável LANG devidamente configurada. Ex:
    export LANG=pt_BR.utf8

Ou informe através do CLI argument. Ex: '--lang=en_US'

Ou o usuário terá que digitar.

Execução:
    python3 hello.py
    ou
    ./hello.py
""" 

# metadadados
__version__ = "0.1.3"
__author__ = "João Paulo Rolim"
__license__ = "Unlicense" 

import os
import sys

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError: not enough values to unpack
    # print(arg[2:].split("="))   
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit()
    #print(f"{key}: {value}")
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:
    os_lang = os.getenv("LANG")  # 'C.UTF-8'
    if os_lang is None:
        current_language = input("Choose a language: ")
    else:
        current_language = os_lang.split(".")[0]
    # current_encoding = os_lang.split(".")[1]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
    "C": "Olá, Mundo !!!",
}

# Busca O(1) - constante por causa da Hash Table
if current_language not in msg:
    print(f"Não existe msg definida para '{current_language}'.")
    sys.exit()

print( msg[current_language] * int(arguments["count"]) )

# export LANG=it_IT.utf8 
# export LANG=C.UTF-8 
