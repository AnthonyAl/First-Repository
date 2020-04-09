
def newVertex(x):
    global k
    global c
    global G
    if(x >= m):
        return 0
    else:
        if(G[H[k - 1]][x] == 1):
            i = 0
            while(i <= k):
                if(H[i] == x):
                    break
                i += 1
            if(i < k):
                c = x + 1
                return 1
            else:
                if(k == m-1):
                    if(G[0][x] == 1):
                        c = x
                        return 2
                    else:
                        c = x + 1
                        return 3
                else:
                    c = x
                    return 4
        else:
            c = x + 1
            return 5

#===============================================================#

def findHamilton():
    global c
    global k
    global H
    global m
    answer = ""
    count = 0
    v = newVertex(H[k] + 1)
    while(count < 100000000): # Takes really long after Q5 :( 
    
        count += 1
    
        if(v == 0): # The next Vertex is out of range -> Go Back.
        
           #print("0",k)
            
            H[k]=-1
            k = k - 1
            if(k > 0): # In this case we can still go back a step.
                v = newVertex(H[k] + 1)
            else: # In this case we've chacked every single possibility with no success, the search for a Hamiltonian cycle has been unsuccessful.
                print("Found Nothing! \n\n\n")
                break
                
        elif(v == 1): # The Vertex in question is already in the circuit -> Check the next Vertex.
        
            #print("1",k,c)
        
            v = newVertex(c)
            
        elif(v == 2): # The search for a Hamiltonian cycle has been successful! -> print the result.
        
            #print("2",k,c)
        
            H[k] = c
            H.append(0)
            for i in range(0, m + 1):
                answer = answer + " " + str(H[i])
            print("Found cycle:", answer, "\n\n\n")
            break
            
        elif(v == 3): # The Vertex in question does not connect with the first cycle Vertex -> Check the next Vertex.
        
            #print("3",k,c)
        
            v = newVertex(c)
            
        elif(v == 4): # The Vertex in question is a valid pick -> Use it in the Hamiltonian cycle and repeat.
        
            #print("4",k,c)
        
            H[k] = c
            #print(H)
            k = k + 1
            v = newVertex(H[k] + 1)
            
        elif(v == 5): # The Vertex in question is not connected to the previous cycle Vertex -> Check the next Vertex.
        
            #print("5",k,c)
        
            v = newVertex(c)
 
 
#======================================================================================#
#======================================================================================#


def isPowerOfTwo( x ): 
    return x and (not(x & (x - 1))) 

#===============================================================#

def differAtOneBitPos( a , b ): 
    return isPowerOfTwo(a ^ b)

#===============================================================#

def createHypercube(n):
    global G
    global m
    for i in range(0,m):
        M=[]
        for j in range (0,m):
            if (differAtOneBitPos(i, j)):
                M.append(1)
            else:
                M.append(0)
        G.append(M)
    for i in range (0, m):
        print(G[i])


#======================================================================================#
#======================================================================================#


while(True):
    print("(Give Q to terminate.)")
    n = input("Give a natural number n: ")
    if(n == "Q" or n == "q"):
        print("Terminating. . . \n\n\n")
        break
    try:
        val = int(n)
        if(val > 1):
            m = 2 ** val
            G = []
            k = 1
            H=[0,]
            for i in range(1, m):
                H.append(-1)
            #print(H)
            #print(val, "\n")
            createHypercube(val)
            findHamilton()
        elif(val == 1):
            print("This graph does not have a Hamiltonian cycle.\n")  
        else:
            print("Number given is not a natural.\n")
    except ValueError:
        print("Please ensure that the input is a number rather than a string.\n")