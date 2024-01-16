#!/usr/bin/env python3
"""emails.py

Programa que prepara o envio de emails através de um template com placeholders.

Como usar:


Execução:
    python3 emails.py
    ou
    ./emails.py
""" 

# metadadados
__version__ = "0.1.0"
__author__ = "João Paulo Rolim"
__license__ = "Unlicense" 

import sys
import os

arguments = sys.argv[1:]
if not arguments:
    print("Informe o nome do arquivo de email")
    sys.exit(1)

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) # emails.txt
templatepath = os.path.join(path, templatename) # email_tmpl.txt

for line in open(filepath):
    name, email = line.split(",")

    # TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")

    print(
        open(templatepath).read() 
        % {
            "nome": name,
            "produto": "caneta",
            "texto": "escrever muito bem!!",
            "link": "https//canetaslegais.com",
            "quantidade": 2,
            "preco": 50.5
        }
    )
    print("-" * 50)
