
#def FindCatalan(n):
    #a = 1;
    #for i in range(1, 2 * n + 1):
    #    a *= i
    #    if(i == n): temp1 = a
    #    elif(i == n + 1): temp2 = a                    #slightly off.
    #    elif(i == 2*n): temp3 = a
    #print(temp3, temp2, temp1)
    #result = temp3 / (temp2 * temp1)
    #return int(result) 
    #==================================================#
    #temp = 1
    #result = 1
    #for i in range(0, n):                               #slightly off.
    #    result =  (2 * (2 * i + 1) / (i + 2)) * temp
    #    temp = result
    #return int(result);
    #==================================================#
    #result = 1
    #for k in range(2, n + 1):                           #slightly off.
    #    result *= (n + k) / k
    #return int(result)
    #==================================================#

#=======================================================================================#

def findCatalan(n):
    temp = [1,]
    for i in range(1, n + 1):    
        result = 0
        for k in range(0, i):
            result += temp[k] * temp[i - 1 - k]
        temp.append(int(result))
    return int(result)

#=======================================================================================#

while True:
    print("(Give Q to terminate.)")
    n = input("Give a natural number n: ")
    if(n.upper() == "Q"):
        print("Terminating. . .\n\n")
        break;
    try:
        n = int(n)
        if(n < 0): print("There was an error in your input. Please make sure you are giving only natural numbers.\n")
        else: 
            result = findCatalan(n)
            print("The", str(n) + "th Catalan number is equal to:", result, "\n\nGo again?\n\n")
    except ValueError: print("There was an error in your input. Please make sure you are giving only natural numbers.\n")