import math
import os
import random
import re
import sys


#
# Complete the 'getTraversals' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING input as parameter.
#
'''
firstdict = {}
second_string = ""
def sort_string1(input):
    first_string = ""
    sort_list1 = input.split()
    alphabetical = sort_list1.sorted()
    firstdict.update({input[0]:0})
    
    while True:
        number = 0
        place = 1
        letter = sort_list1[place]
        pletter = sort_list1[place-1]
        if alphabetical.index(letter):
            alphabetical.index(pletter)
            firstdict.update({letter:number+1})
            
    
    return first_string
'''
class Node:
    
    def __init__(self,letter):
        
        self.left = None
        self.right = None
        self.letter = letter
        
    def insert(self,letter):
        if self.letter:
            if str(letter) <=str(self.letter):
                if self.left is None:
                    self.left = Node(letter)
                else:
                    self.left.insert(letter)
            elif str(letter) > str(self.letter):
                if self.right is None:
                    self.right = Node(letter)
                else:
                    self.right.insert(letter)
        else:
            self.letter = letter
    def firststringSort(self, letters):
        firststring = []
        if letters:
            firststring.append(letters.letter)
            firststring = firststring + self.firststringSort(letters.left)
            firststring = firststring + self.firststringSort(letters.right)
        return firststring
    def secondstringSort(self,letters):
        secondstring = []
        if letters:
            secondstring = self.secondstringSort(letters.left)
            secondstring = secondstring + self.secondstringSort(letters.right)
            secondstring.append(letters.letter)
        return secondstring
            
def getTraversals(input):
    letters = Node(input[0])
    for i in range(1,len(input)):
        letters.insert(input[i])
    result = ''.join(letters.firststringSort(letters)) + " " + ''.join(letters.secondstringSort(letters))
    return result
    #return sort_string1(input)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    input = input()

    result = getTraversals(input)

    fptr.write(result + '\n')

    fptr.close()
