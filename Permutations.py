
def printP(p, chr, strg):
    prnt = chr +" = { "
    print("\n\n")
    print(strg, "\n")
    for i in range(len(p)): prnt += "(" + str(i + 1) + "," + str(p[i]) + ")" + " "
    prnt += "}"
    print(prnt)

#===================================================================================#

def reverseP(r):
    P = []
    p = []
    for i in r:
        p.append(i)
    for i in range(len(r)):
        P.append(i + 1)
    for i in range(len(r)):
        min = p[i]
        for j in range(i + 1, len(r)):
            if(p[j] < min):
                min = p[j]
                temp = p[i]
                p[i] = p[j]
                p[j] = temp
                temp = P[i]
                P[i] = P[j]
                P[j] = temp
    printP(P, "f -1", "The reversed permutation is:")
    
#===================================================================================#

def cycleDecomposition(p):
    strg = ""
    P = []
    temp = []
    temp1 = []
    x = 0
    for i in range(len(p)):
        P.append(i+1)
    while True:
        try:
            y = P[0]
            temp.append(y)
        except IndexError: break
        while True:
            z = p[x]
            temp.append(z)
            P.pop(x)
            p.pop(x)
            for i in range(len(P)):
                if(z == P[i]):
                    x = i
            if(z == y): 
                temp1.append(temp)
                temp = []
                x = 0
                break
    for i in range(len(temp1)): 
        if(len(temp1[i]) > 2): strg += "( "
        for j in range(len(temp1[i]) - 1): 
            if(len(temp1[i]) > 2): strg += str(temp1[i][j]) + " "
        if(len(temp1[i]) > 2): strg += ") "
    print("\n\nThe permutation after the cycle decomposition:\n")
    print(strg, "\n\n")
    cycleTranspositions(temp1)

#===================================================================================#

def cycleTranspositions(p):
    strg = ""
    temp = []
    for i in range(0, len(p)):
        for j in range(len(p[i]) - 2, 0, -1):
            temp.append((p[i][0], p[i][j]))
    for i in temp:
        strg += "( "
        for j in i: strg += str(j) + " "
        strg += ") "
    print("The permutation as a product of transpositions is:\n")
    print(strg, "\n\n")
    if(sgn(temp)): print("The permutation is EVEN\n\n")
    else: print("The permutation is ODD.\n\n")

#===================================================================================#

def sgn(p):
    if(len(p) % 2 == 0): return True
    else: return False

#===================================================================================#

class NotNaturalError(Exception):
    def __init__(self):
        self.message = None
    def __str__(self):
        return "NotNaturalError has been raised."

#--------------------<                                     >--------------------#

while True:
    print("(Give Q to terminate.)")
    p = input("Give a permutation p (with spaces between each number): ")
    if(p == "Q" or p == "q"): 
        print("Terminating . . . \n\n\n")
        break
    check = True
    check1 = False
    P = []
    p = p.split()
    for i in p:
        try:
            i = int(i)
            if(i <= 0): raise NotNaturalError
            else:
                P.append(i)
        except ValueError: 
            print("\n Please ensure that your input consists of natural numbers.\n\n")
            check = False
            break
        except NotNaturalError: 
            print("\n Each given number of the permutation must be a natural.\n\n")
            check = False
            break
            
    if(check):
        temp = []
        for i in range(len(P)):
            temp.append(i+1)
        if(P == temp): 
            check = False
            check1 = True
        temp1 = []
        for i in P:
            temp1.append(i)
        temp1.sort()
        if(temp1 != temp): 
            print("\n\nYour input has a mistake. It does not look like a permutation!\n\n")
            check = False
            
    if(check1):
        printP(P, "e", "The given permutation is the Identity permutation ():")
        print("\n\nThe length of the permutation is:", len(P))
        printP(P, "e -1", "The permutation reversed is the Identity permutation ():")
        print("\nThe Identity permutation is a cycle (the only one) of length 1.\n")
        print("The Identity permutation as a product of transpositions is simply:\n() = ( 1 2 ) ( 1 2 ) \n\n")
        print("The Identity permutation is always EVEN.\n\n")
        
    if(check):
        printP(P, "f", "The given permutation is:")
        print("\n\nThe length of the permutation is:", len(P))
        reverseP(P)
        if(len(P) > 1):
            cycleDecomposition(P)