#!/usr/bin/env python3
"""Calculadora Prefix.

Funcionamento:

[operacao] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5
50

$ prefixcalc.py 
Digite a operação: sum
Digite o 1° número: 5
Digite o 2° número: 4
9

""" 

# metadadados
__version__ = "0.1.0"
__author__ = "João Paulo Rolim"
__license__ = "Unlicense" 

import sys

args = sys.argv[1:]

if not args:
    args.append(input("Digite a operação: "))
    args.append(input("Digite o 1° número: "))
    args.append(input("Digite o 2° número: "))
elif len(args) != 3:
    print("Número de argumentos inválido!")
    print("Exemplo correto: sum 3 7")
    sys.exit(1)

op, n1, n2 = args

n1 = int(n1)
n2 = int(n2)

if op == 'sum':
    print(n1 + n2)
elif op == 'sub':
    print(n1 - n2)
elif op == 'mul':
    print(n1 * n2)
elif op == 'div':
    if n2 == 0:
        print("Não é possível divisão por 0.")
        sys.exit(1)
    else:
        print(n1 / n2)
else:
    print("Operação não suportada. Tente: 'sum', 'sub', 'mul' ou 'div'.")
    sys.exit(1)
