
def printP(p, chr, strg):
    prnt = chr +" = { "
    print("\n\n")
    print(strg, "\n")
    for i in range(len(p)): prnt += "(" + str(i + 1) + "," + str(p[i]) + ")" + " "
    prnt += "}\n"
    print(prnt)
    prnt = "Or in other words: "
    for i in range(len(p)): prnt += str(p[i]) + " "
    print(prnt)

#==================================================================================================#

def factorial(x):
    fact = 1
    for i in range(x):
        fact *= (i + 1)
    return fact

#==================================================================================================#

def findRank(s):
    temp = []
    temp.extend(s)
    rank = 0
    for i in range(len(s) - 1, 0, -1):
        rank += (temp[0] - 1) * factorial(i)
        s1 = temp.pop(0)
        for j in range(len(temp)):
            if(s1 < temp[j]): temp[j] -= 1
    return rank

#===================================================================================================#

while True:
    print("(Give Q to terminate.)")
    p = input("Give a permutation p (with spaces between each number): ")
    if(p.upper() == "Q"): 
        print("Terminating . . . \n\n\n")
        break
    check = True
    P = []
    p = p.split()
    for i in p:
        try:
            i = int(i)
            if(i <= 0): 
                print("\n Each given number of the permutation must be a natural.\n\n")
                check = False
                break
            else:
                P.append(i)
        except ValueError: 
            print("\n Please ensure that your input consists of natural numbers.\n\n")
            check = False
            break   
    if(check):
        temp = []
        for i in range(len(P)):
            temp.append(i+1)
        temp1 = []
        for i in P:
            temp1.append(i)
        temp1.sort()
        if(temp1 != temp): 
            print("\n\nYour input had an error. It does not look like a permutation!\n\n")
            check = False
    if(check):
        printP(P, "f", "The given permutation is:")
        print("\nThe rank of this permutation is: \n rank"+ str(len(P)) +"(p) = " + str(findRank(P)) + "\n")