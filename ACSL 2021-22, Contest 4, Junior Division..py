
def absv(a, b):
    return math.sqrt(a**2 + b**2)

def f(i, a, b):
    if i==0: 
        return [a, b]
    fz = f(i-1, a, b)
    bia = (fz[0]**2 - fz[1]**2) + a 
    bib = 2*fz[0]*fz[1] + b
    return [bia, bib]


def iterate(a, b):
    z = 0
    ab =0 
    while z <= 4 and ab <4:
        c = f(z, a, b)
        ab= absv(float(c[0]),float(c[1]))
        z = z+1
    if ab > 4:
        return ("ESCAPES " + str(z))
    else:    
        return str(round(ab,3))
        

        
        
def absResult(realPartC, imagPartC):
    return iterate(realPartC, imagPartC)
