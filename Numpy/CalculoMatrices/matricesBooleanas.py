# /usr/bin/env python3
import numpy as np 

def matrices():
    np.random.seed(0)
    x= np.random.randint(0,72,size=(4,9))
    print(x)
    a= np.count_nonzero(x>6)
    print(a)
    a=np.sum(x>6, axis=1)
    print(a)
    #podemos usar np.any() o np.all()
    b=np.any(x>9)
    if b:
        print("Al menos hay un valor mayor en 'a' que 9")
    b=np.all(x>0)
    if b:
        print("Todoos los valores de a son mayores a 0")
    else:
        print("Todos los valores sno son mayores a '0'")

if __name__=="__main__":
    matrices()