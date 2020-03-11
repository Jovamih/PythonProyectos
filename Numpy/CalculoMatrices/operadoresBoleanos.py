# /usr/bin/env python3
import numpy as np 
import sys
def operator_boolean(n0=0,n1=0):
    a=np.random.randint(1,80,size=(9,9))
    mul6y7= (np.mod(a,n0)==0 )& (np.mod(a,n1)==0)
    #enmascaramiento
    b=a[mul6y7]
    print(a)
    if mul6y7.any():
        print("Existe al menos un valor multiplo de {} y {}".format(n0,n1))
    print(b)
    
if __name__=="__main__":
    if len(sys.argv)<3:
        print("Faltan valores")
    operator_boolean(int(sys.argv[1]),int(sys.argv[2]))