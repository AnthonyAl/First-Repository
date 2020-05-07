
def findStrilring(n, k):
    a = []
    b = []
    for i in range(1, n + 1):
        del b[:]
        b.extend(a)
        del a[:]
        for j in range(1, i + 1):
            if(j == 1 or j == i): a.append(1)
            else:
                temp = j * b[j - 1] + b[j - 2]
                a.append(temp)
    return a[k - 1]

#=======================================================================================#

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
        n, k = int(n), int(k)
        if(n < 0 or k < 0 or k > n): print("There was an error in your input. Remember to give only natural numbers.\n")
        else: 
            result = findStrilring(n, k)
            print("The Stirling number of the second kind", "S(" + str(n) + ", " + str(k) + ")","is equal to:", result, "\n\nGo again?\n\n")
    except ValueError: print("There was an error in your input. Remember to give only natural numbers.\n")