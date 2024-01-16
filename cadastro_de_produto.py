#!/usr/bin/env python3
"""Cadastro de Produto"""

# metadadados
__version__ = "0.1.0"
__author__ = "João Paulo Rolim"
__license__ = "Unlicense" 

produto = {
    "nome" : "Caneta",
    "cores" : ["azul","preto"],
    "preco" : 3.23,
    "dimensao": {
        "altura" : 12.1,
        "largura" : 0.8,
    },
    "em_estoque" : True,
    "codigo" : 45678,
    "codebar" : None,
}

cliente = {
    "nome": "Bruno",
    "sobrenome": "Rocha"
}

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

total_compra = compra["quantidade"] * compra["produto"]["preco"]

print(
    f"O cliente {compra['cliente']['sobrenome']}"
    f" comprou {compra['quantidade']} unidades"
    f" de {compra['produto']['nome']} (cod: {compra['produto']['codigo']})"
    f" e pagou o total de {total_compra}"
)

