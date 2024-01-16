#!/usr/bin/env python3
""" Imprime a tabuada do 1 ao 10.

---Tabuada do 1---

     1 x 1 = 1
     1 x 2 = 2
     1 x 3 = 3
...
###################
---Tabuada do 2---

     2 x 1 = 2
     2 x 2 = 4
     2 x 3 = 6
...
###################
...
"""

# metadadados
__version__ = "0.1.1"
__author__ = "João Paulo Rolim"
__license__ = "Unlicense" 

numeros = list(range(1,11))

for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()

    for n2 in numeros:
        result = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {result}"))
    
    print("#" * 18)
    print()
