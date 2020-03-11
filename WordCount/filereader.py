#! usr/bin/env python3
import sys
def filereader(path):
    with open(path,"r") as f:
        lines=f.read()
    return lines

if __name__=="__main__":
    if len(sys.argv)<2:
        print("filereader --<path> : Incluya la ruta del archivo")
        exit(1)
    fpath=sys.argv[1]
    try:
        text=filereader(fpath)
        print(text)
    except Exception as e:
        print(e,file=sys.stderr)
    