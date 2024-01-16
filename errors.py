#!/usr/bin/env python3

import sys
import os

# LBYL - Look Before You Leap

if os.path.exists("names.txt"):
    print("O arquivo existe")
    input("...")  # Race Condition
    names = open("names.txt").readlines()
else:
    print("[Error] File 'names.txt' not found.")
    sys.exit(1)    

index = 1

if len(names) >= index + 1:
    print(names[index])
else:
    print("[Error] Missing name in the list.")
    sys.exit(1)