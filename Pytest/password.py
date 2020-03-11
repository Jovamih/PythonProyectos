# /usr/bin/env python3
import sys

key=0
phrasse_real=str()
phrasse_possible=str()
result=False
def genesis(phrasse_found=str(),exec=0):
    global key
    global result
    if exec>0:
        for l in phrasse_possible:
            result =genesis(phrasse_found+l,exec-1)
            if result:
                break
    else:
        key=key+1
        print('\r {} keys tested! => Actual: {}'.format(key,phrasse_found),end='')
        if phrasse_real==phrasse_found:
            print('\nphrasse found= {}'.format(phrasse_found))
            return True

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Parametros: <password.py> <key_original> <key_possible> <n_caracteres>")
        exit(0)
    #key=0
    phrasse_real=sys.argv[1]
    phrasse_possible=sys.argv[2]
    exec=int(sys.argv[3])
    result=False
    try:
        phrasse_found=str()
        result=genesis(phrasse_found,exec)
    except Exception as e:
        print(e)