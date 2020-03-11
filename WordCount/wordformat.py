#! usr/bin/env python3
import sys

def wordformat(word):
    print(word.capitalize())
    print(word.title())
    print(word.lower())
    print(word.upper())
    print(word.swapcase())
    print(word.center(50,"="))

if __name__=="__main__":
    if len(sys.argv)<2:
        print("wordformat --<word> : Especifique la palabra a formatear")
        exit(1)
    word=sys.argv[1]
    wordformat(word)
