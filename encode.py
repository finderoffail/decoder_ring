#!/usr/bin/python3
import sys
import re

decoder = {'A':4, 'B':7, 'C':5, 'D':9, 'E':6, 'F':8, 'G':10, 'H':24, 'I':1, 'J':25, 'K':15, 'L':14, 'M':12, 'N':13, 'O':3, 'P':11, 'Q':16, 'R':17, 'S':23, 'T':26, 'U':21, 'V':19, 'W':18, 'X':20, 'Y':22, 'Z':2}

inputStr = re.sub('[^A-Z ]','',sys.argv[1].upper())
print("input =", inputStr)
print("output =")
firstChar = True;
for c in inputStr:
    if c==' ':
        print('')
        firstChar = True;
    else:
        if firstChar == True:
            firstChar = False
        else:
            print(' - ',end='')
        print(decoder.get(c),end='')
print('')
