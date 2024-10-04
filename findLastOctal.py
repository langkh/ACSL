#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findLastOctal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def StrToBin(s):#converts string to binary
    sent_binary = ""
    for i in s:
        ascii = ord(i)
        char_binary = bin(ascii)
        char_binary = char_binary.replace("b","")
        if len(char_binary) < 8:
            sent_binary += "0"+char_binary
        else:
            sent_binary += char_binary
    return sent_binary
def findLastbin(s):
    bin_string = StrToBin(s)

    counter = 0 #the nuber of times you have been searching for a number
    binCounter = "0" #The number you are searching for
    reverse_bin_string = bin_string[::-1]
    binCounter = bin(counter)
    binCounter = binCounter.replace("0b","")
    print(bin_string)
    while binCounter in bin_string:
        binCounter = bin(counter)
        binCounter = binCounter.replace("0b","")
        print(binCounter)
        if binCounter in bin_string and binCounter[::-1] in reverse_bin_string:
            bin_string = bin_string.replace(binCounter,"",1)
            reverse_bin_string = bin_string[::-1]
            reverse_bin_string = reverse_bin_string.replace(binCounter[::-1],"",1)
            bin_string = reverse_bin_string[::-1]
            print(bin_string)
            counter+=1
        elif binCounter not in bin_string:
            break
        else:
            bin_string = bin_string.replace(binCounter,"",1)
            counter += 1
    return bin_string
    
              
def findLastOctal(s):
    bin_string = int(findLastbin(s))
    oct_string = oct(bin_string)
    oct_string = oct_string.replace("0o","")
    print(oct_string)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = findLastOctal(s)

    fptr.write(str(result) + '\n')

    fptr.close()
