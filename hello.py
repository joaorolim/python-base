#!/usr/bin/env python3
"""Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente, o programa exibe a mensagem
correspondente.

Como usar:
Tenha a variável LANG devidamente configurada. Ex:
    export LANG=pt_BR

Execução:
    python3 hello.py
    ou
    ./hello.py
""" 

# metadadados
__version__ = "0.0.1"
__author__ = "João Paulo Rolim"
__license__ = "Unlicense" 

import os

os_lang = os.getenv("LANG", "en_US.utf8")  # 'C.UTF-8'
current_language = os_lang.split(".")[0]
current_encoding = os_lang.split(".")[1]

msg = f"Hello, World! - {current_language}.{current_encoding}"

if current_language == "pt_BR":
    msg = f"Olá, Mundo! - {current_language}.{current_encoding}"
elif current_language == "it_IT":
    msg = f"Ciao, Mondo! - {current_language}.{current_encoding}"

print(msg)
