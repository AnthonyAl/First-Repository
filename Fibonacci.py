
def findFibonacci(n, f0, f1):
    temp1 = f0
    temp2 = f1
    if(n == 0): return temp1
    elif(n == 1): return temp2
    else:
        for i in range(2, n + 1):
            answer = temp1 + temp2
            temp1 = temp2
            temp2 = answer
        return answer

#=======================================================================================#

asked = False;
while True:
    try:
        if(not asked):
            print("Give the first two numbers of the sequence, F(0), F(1). These will remain unchanged throughout this run of the program.\n")
            f0 = int(input("Give the first, F(0): "))
            f1 = int(input("Give the second F(1): "))
            asked = True
    except ValueError: 
        print("There was an error in your input. Please make sure you are giving only natural numbers.\n")
        asked = False
    if(asked):
        print("(Give Q to terminate.)")
        n = input("Give a natural number n: ")
        if(n.upper() == "Q"):
            print("Terminating. . .\n\n")
            break;
        try:
            n = int(n)
            if(n < 0): print("There was an error in your input. Please try giving a natural number once again.\n")
            else: 
                print("The", str(n) + "th Fibonacci number is equal to:", int(findFibonacci(n, f0, f1)), "\n\nGo again?\n\n")
        except ValueError: print("There was an error in your input. Please make sure you are giving only natural numbers.\n")