def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n-1)+fib(n-2)


def fibCypher(key, msg):
    message = []
    MSG = []
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in msg:
        MSG.append(i)
    print(MSG)
    keyindex = alphabet.index(key)+1
    index = 1
    for letter in MSG:
        fibindex = fib(index)
        index = index + 1
        fiboffsetIndex = fibindex+keyindex

        if fiboffsetIndex <=26: 
            fibboffset = alphabet[fiboffsetIndex-1]
        elif fiboffsetIndex > 26:
            fibboffset = alphabet[fiboffsetIndex%26 -1]
        
        message.append((ord(letter) +ord(fibboffset)))
        answer = ' '.join([str(i) for i in message])
    return answer
