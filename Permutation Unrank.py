
def printP(p, chr):
    prnt = chr +" = { "
    for i in range(len(p)): prnt += "(" + str(i + 1) + ", " + str(p[i]) + ")" + " "
    prnt += "}\n"
    print(prnt)
    prnt = "Or in other words: "
    for i in range(len(p)): prnt += str(p[i]) + " "
    print(prnt)

#======================================================================================================================#

def factorial(x):
    fact = 1
    for i in range(x):
        fact *= (i + 1)
    return fact

#======================================================================================================================#

def findPermutation(n, k):
    fact_seq = []
    temp = k
    for i in range(n - 1, 0, -1):
        di = temp // factorial(i)
        while(i < di):
            di -= 1
        fact_seq.append(di)
        temp -= di * factorial(i)
    #-------------------------------------#
    permutation = [1,]
    for di in reversed(fact_seq):
        for i in range(len(permutation)):
            if(di < permutation[i]): permutation[i] += 1
        permutation.insert(0, di + 1)
    return permutation

#======================================================================================================================#

while True:
    print("(Give Q to terminate.)")
    n = input("Give a natural number n: ")
    if(n.upper() == "Q"):
        print("Terminating. . .\n\n")
        break;
    k = input("Give a natural number k: ")
    if(k.upper() == "Q"):
        print("Terminating. . .\n\n")
        break;
    try:
        n = int(n)
        k = int(k)
        if(n < 1 or k < 0): print("There was an error in your input. Please make sure you are giving only natural numbers.\n")
        else: 
            if(k >= factorial(n)): k = factorial(n) - 1
            result = findPermutation(n, k)
            print("\nThe", str(k) + "th ranked permutation of [" + str(n) + "] is:\n")
            printP(result, "f")
            print("\n\nGo again?\n\n")
    except ValueError: print("There was an error in your input. Please make sure you are giving only natural numbers.\n")