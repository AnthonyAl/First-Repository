
def gcd(x, y): 
   while(y): 
       x, y = y, x % y 
   return x

#===================================================================================#

def lcm(x, y):
    lcm = int(x * y / gcd(x, y))
    return lcm

#===================================================================================#

def maxOrder(n):
    max = 1
    halfn = int(n/2)
    for i in range(halfn):
        if(lcm(i + 1, n - i - 1) > max): max = lcm(i + 1, n - i - 1)
    return max

#===================================================================================#

while True:
    print("(Give Q to terminate.)")
    n = input("Give a natural number n: ")
    if(n == "Q" or n=="q"):
        print("\nTerminating. . .\n\n")
        break
    try:
        n = int(n)
        if(n < 2): print("\nYour input was incorrect. Please ensure that you give a natural number. \n\n")
        else:
            print("\nThe maximum possible order for a permutation of [", n, "], that is a product of two distinct cycles of a combined length of", n, ", is:", maxOrder(n), "\n\n")
    except ValueError: print("\nYour input was incorrect. Please ensure that you give a natural number, not a string. \n\n")