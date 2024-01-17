#!/usr/bin/env python3

import sys
import os

# # LBYL - Look Before You Leap

# if os.path.exists("names.txt"):
#     print("O arquivo existe")
#     input("...")  # Race Condition
#     names = open("names.txt").readlines()
# else:
#     print("[Error] File 'names.txt' not found.")
#     sys.exit(1)    

# index = 1

# if len(names) >= index + 1:
#     print(names[index])
# else:
#     print("[Error] Missing name in the list.")
#     sys.exit(1)


# EAFP - Easy to Ask Forgiveness than Permission

try:
    print("Antes do Raise")
    raise RuntimeError("[RuntimeError] Ocorreu um erro")
    print("Depois do Raise")
except Exception as e:
    print(f"{str(e)}")
    # sys.exit(1)

try:
    names = open("names.txt").readlines() # FileNotFoundError
    1 / 1 # ZeroDivisionError
    names.append("Sergio")
    print(names.append) # AttributeError
# except: # Bare Except
except (FileNotFoundError, 
        ZeroDivisionError,
        AttributeError ) as e:
    print(f"{str(e)}")
    sys.exit(1)    
    # TODO: Usar retry
else:
    print("Sucesso!")
finally:
    print("Execute isso sempre")


index = 3

try:
    print(names[index])
    print(names[index + 1])
except:
    print("[Error] Missing name in the list.")
    sys.exit(1)