
def print_euler(n):
    v=[]
    e=[]
    ans=[]
    for i in range (0,n):
        v.append(i)
    for i in range (0,n-1):
        for j in range (i+1,n):
            e.append((i, j))
    print("\n\n Vertices: \n", v, "\n\n Edges: \n", e, "\n")
    t1=0
    t2=e[0][1]
    ans.append((e[0][0], e[0][1]))
    for x in range (0,int(n*(n-1)/2)-1):
        e.pop(t1)
        t4=1
        t5=-1
        for i in e:
            t5+=1
            if(t4 == 1):
                if(t2==e[t5][0]):
                    t3=0
                    t4=0
                    t2=e[t5][1]
                    t1=t5
        t5=-1
        for i in e:
            t5+=1
            if(t4 == 1):                        
                if(t2==e[t5][1]):
                    t3=1
                    t4=0
                    t2=e[t5][0]
                    t1=t5
        if(t3 == 1):
            ans.append((e[t1][1], t2))
        elif(t3 == 0):
            ans.append((e[t1][0], t2))
    #print the final answer.
    n = "K" + str(n)
    j = -1
    answer = ""
    print("\n\n Example of an Eulerian Circuit for the graph", n, ": \n")
    for i in ans:
        j+=1
        answer = answer + " " + str(ans[j][0])
    print(answer, "0 \n\n")
   
#--------------------------------------------------------------------------------------------------------------------#

def is_euler(n):
    if(n == 1):
        return False
    elif(n == 2):
        return False
    elif((n - 1) % 2 == 1):
        return False
    else:
        return True

#--------------------------------------------------------------------------------------------------------------------#

while True:
    print("(Give Q to terminate.)")
    n = input("Give a natural number n: ")
    if(n == "q" or n == "Q"):
        print("Terminating. . . \n\n\n ")
        break
    try:
        val = int(n)
        if(val > 0):    
            if(is_euler(val) == False):
                print(" n =",val, "\n Since for the graph Kn the degree is n-1, ")
                val = " K" + str(val)
                print(val, "does not have an Eulerian Circuit. \n")
            else:
                print_euler(val)
        else:
            print("Number given is not a natural.. \n")
    except ValueError:
        print("Please ensure that your input is a number and not a string.\n")
