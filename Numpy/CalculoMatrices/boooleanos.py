# /usr7bin/env python3
import numpy as np 

def compare():
    a=np.array([12,34,45,67,78])
    b=np.array([98,12,34,3,45])
    
    print(a==b)
    print(np.equal(a,b))
    print(a<b)
    print(np.less(a,b))
    print(a>b)
    print(np.greater_equal(a,b))
        
if __name__=="__main__":
    compare()