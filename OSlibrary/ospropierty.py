# /usr/bin/env python3
import sys
from os import path as p 
import os

def os_propiertys():
    print(os.path)
    print(os.name)
    print(os.curdir)
    print(os.listdir(os.curdir))
    print(os.pardir)
def path_propiertys():
    print(p.abspath(os.curdir))
    print(p.dirname(os.curdir))
if __name__=="__main__":
    os_propiertys()
    path_propiertys()