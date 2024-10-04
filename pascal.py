def pascaltrilist():
    megalist =[]
    list=[1] 
    megalist.append(list)
    for i in range(30):  
        newlist=[] 
        newlist.append(list[0]) 
        for i in range(len(list)-1): 
            newlist.append(list[i]+list[i+1]) 
        newlist.append(list[-1]) 
        list=newlist
        megalist.append(list)
    return megalist

 

def fib(n):
    fibs = [1, 1]
    while len(fibs) <= n:
        next_value = fibs[len(fibs) - 1] + fibs[len(fibs) - 2]
        fibs.append(next_value)
    return  fibs 
def findindex(fibNumber):
    fibs = fib(30)
    if fibNumber in fibs:
        fibdex=fibs.index(fibNumber)
        return fibdex
    else: 
        return -1
def findnums(fibNumber):
    megalist = pascaltrilist()
    sums = []
    fibdex = findindex(fibNumber)
    if fibdex == -1:
        print("not there buddy")
    i = fibdex
    j = 0
    while (i > 0) :
        sums.append(megalist[i][j])
        if sum(sums) == fibNumber:
            return sums
        i= i-1
        j= j+1
def printNumbers(fibNumber):
    findindex(fibNumber)
    answer = findnums(fibNumber)
    
    if fibNumber > 1 and answer != None:
        mystring = str(answer[0])
        strlen = len(answer)
        for i in range(1,strlen):
            mystring += " " + str(answer[i])
        return mystring
    else: 
        return str(fibNumber)
        
   
        
