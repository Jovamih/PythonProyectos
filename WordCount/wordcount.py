#! /usr/bin/env python3
import sys

def word_count(text):
    word= text.split(" ")
    return len(word)

def lines_count(text):
    lines= text.split("\n")
    for l in lines:
        if not l :
            lines.remove(l)
    return len(lines)

if __name__=="__main__":
    
    if len(sys.argv)<2:
        print("Ingrese la ruta del archivo",file=sys.stderr)
        exit(1)
        
    filename= sys.argv[1]
    with open(filename,"r") as f:
        text=f.read()
        num_word=word_count(text)
        num_lines=lines_count(text)
        print("Number of Words:",num_word)
        print("Number of lines:",num_lines)

