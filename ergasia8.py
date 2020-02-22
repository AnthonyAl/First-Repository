import random

value=[]
for _ in range(3):
	value.append(random.randrange(0, 101)) #BEHOLD THE CARS!!


while(True):
    r=input("Tap enter to continue or type 'S' to exit the algorithm.\n")
    if(r=="S"):
        break
    light=[0,0,0]
    M=max(value)
    print("The value list is as following:", value)
    print("\nThe max value is ", M, ".")

    for i in range(3):
        if(value[i]==M):
            j=i
            break
            
    light[i]=1
    print("\nThe lights' states are: ", light, "\n\n")
    
    vfg=random.randrange(5,11)
    value[i]-=vfg
    if(value[i]<0): #Negative cars is bad cars. . .
        vfg+=value[i]
        value[i]=0
    for j in range(3):
        if(light[j]==0):
            vfr=random.randrange(0,6)
            value[j]+=vfr
            print("The light no:", j+1, "was red and gained ", vfr, " car(s) in this turn.\n")
            print("Also this light went up to having ", value[j], " car(s) waiting.\n\n")
    print("The light no:", i+1, "was green and lost ", vfg, " car(s) in this turn.\n")
    print("Also this light went down to having just ", value[i], " car(s) remaining.\n\n")
    
print("Exiting. . .\n\n")