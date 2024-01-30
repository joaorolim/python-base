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
import logging

log_level =os.getenv("LOG_LEVEL", "WARNING").upper()
# nossa instancia
log = logging.Logger("mainLog", log_level)
# level
ch = logging.StreamHandler()  # console handler
ch.setLevel(log_level)
# formatação
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
)
ch.setFormatter(fmt)
# destino
log.addHandler(ch)

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    try: 
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use '=', you passed %s, try --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1) 

    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option '{key}'")
        sys.exit(1)
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
# if current_language not in msg:
#     print(f"There's not defined message for '{current_language}'")
#     print(f"Try with {list(msg.keys())}")
#     sys.exit()


# Tenta... Se não conseguir, retorno valor default
# other_message = msg.get(current_language, msg["es_SP"])
# print(other_message)

# EAFP
try:
    message = msg[current_language]
except KeyError as e:
    print(f"[KeyError] {str(e)}")
    print(f"There's not defined message for '{current_language}'")
    print(f"Try with {list(msg.keys())}")
    sys.exit(1)


print( message * int(arguments["count"]) )

# export LANG=it_IT.utf8 
# export LANG=C.UTF-8 
