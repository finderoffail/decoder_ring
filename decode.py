#!/usr/bin/python3
import sys
import re

decoder = {4:'A', 7:'B', 5:'C', 9:'D', 6:'E', 8:'F', 10:'G', 24:'H', 1:'I', 25:'J', 15:'K', 14:'L', 12:'M', 13:'N', 3:'O', 11:'P', 16:'Q', 17:'R', 23:'S', 26:'T', 21:'U', 19:'V', 18:'W', 20:'X', 22:'Y', 2:'Z'}

inputList = re.sub('[^0-9\s]','',sys.argv[1]).split()
print("input =", inputList)
print("output = ", end='')

for i in inputList:
    print(decoder.get(int(i),'?'),end='')

print('')
