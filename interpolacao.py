#!/usr/bin/env python3
"""Interpolacao.py

Programa que prepara o envio de emails através de um template com placeholders.

Como usar:


Execução:
    python3 Interpolacao.py
    ou
    ./Interpolacao.py
""" 

# metadadados
__version__ = "0.1.0"
__author__ = "João Paulo Rolim"
__license__ = "Unlicense" 

email_tmpl = """
Olá, %(nome)s! Tudo bem?!

Tem interesse em comprar %(produto)s?

Este produto é ótimo para %(texto)s

Clique agora em: %(link)s

Apenas %(quantidade)d disponível(is)!

Preço promocional: R$ %(preco).2f

Peça já o seu!!!
"""

clientes = ["Maria","João Rolim","Bruno Rocha"]

for cliente in clientes:
    print(
        email_tmpl %
        {
            "nome": cliente,
            "produto": "caneta",
            "texto": "escrever muito bem!!",
            "link": "https//canetaslegais.com",
            "quantidade": 2,
            "preco": 50.5
        }
    )
