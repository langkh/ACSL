#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'encodeMessage' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING text
#  2. STRING message
#
def splitIntoSentences(text):
    text = text.replace("-"," ")
    text = text.replace("!",".").replace("?",".")
    sentencesText = text.split(".")
    
    
    for i in range(0, len(sentencesText)):
        sentencesText[i] = sentencesText[i].replace("/"," ")
        sentencesText[i] = sentencesText[i].split()
        
    return sentencesText

def findOccurrence(charDict, textArray, letter, goalindex):
    print("Total occurrunces of letter: "+str(charDict[letter]))
    print("goalindex: "+str(goalindex))
    while goalindex > charDict[letter]:
        
        goalindex = goalindex // 2
    print("Goalindex: "+str(goalindex))
    occurrences = 0
    
    for s in range(0, len(textArray)):

        for w in range(0, len(textArray[s])):
            print(textArray[s][w])
            if letter in textArray[s][w]:
                if textArray[s][w].count(letter)==1:
                    
                    occurrences+=1
                    print("Letter: "+letter+" Occurrence: "+str(occurrences)+ " Word: "+textArray[s][w])
                    
                    if occurrences == goalindex:
                        
                        

                        print(str(s+1)+"."+str(w+1)+"." +str(textArray[s][w].index(letter)+1))
                        return str(s+1)+"."+str(w+1)+"." +str(textArray[s][w].index(letter)+1)
                else:
                    letterExistCount = textArray[s][w].count(letter)
                    
                    if occurrences+letterExistCount >= goalindex:
                        letterIndex=0
                        for i in textArray[s][w]:
                            letterIndex+=1
                            if i == letter:
                                
                                
                                occurrences+=1
                               
                                if occurrences == goalindex:
                                    print(str(s+1)+"."+str(w+1)+"." +str(letterIndex))
                                    return str(s+1)+"."+str(w+1)+"." +str(letterIndex)
                    else:
                        occurrences+=letterExistCount
                            
                            
                            
            
def encodeMessage(text, message):
    charDict = {}
    for i in text:
        if i in charDict:
            charDict[i] += 1
        else:
            charDict[i] = 1  
    print(charDict)     
    textArray = splitIntoSentences(text)
    code = ""
    alnumCount = 0
    for i in range(0, len(message)):
        if message[i].isalnum():
            alnumCount+=1
            
            code+= findOccurrence(charDict, textArray, message[i], alnumCount)+" "

        else:

            if code[-1] == " ":   
                code = code[:-1]
                if message[i]==" ":
                    code+="_"
                else:
                    code+=message[i]
            else:
                if message[i]==" ":
                    code+="_"
                else:
                    code+=message[i]
            
    return code
    # Write your code here
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text = input()

    message = input()

    result = encodeMessage(text, message)

    fptr.write(result + '\n')

    fptr.close()
