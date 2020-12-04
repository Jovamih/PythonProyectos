#usr/bin/env python3
# -*- coding:utf-8 -*-
import sys

def name_validate(name=str()):
    if (len(name) in range(6,13)):
        if name.isalnum():
            return True
        else:
            print('El nombre de usuario solo debe contener letras y numeros',file=sys.stderr)
            return False
    else:
        print('El nombre usuario debe estar entre 5 y 12 caracteres',file=sys.stderr)
        return False
    
def pass_validate(pwd=str()):
    mayus,minus,space,num=False,False,False,False
    if len(pwd)>=8:
        pass