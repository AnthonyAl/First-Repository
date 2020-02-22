import itertools

#---------------------------------------------------------------------------------------------------------------|

def check(a,b,c,d,e,f):
    global listt
    bb=[]
    dd=[]
    p=[]
    pp=[]
#η dd είναι η τελική λίστα η οποία περιέχει όλες τις διατάξεις σε σειρά προτεραιότητας.
    l=[a,b,c,d,e,f]
    l[0]=a+" " #θεωρώ το διαχωριστικό στοιχείο των ασκήσεων στο αρχείο να είναι το κενό " ", και το διαχωριστικό στοιχείο των συνδυασμών να είναι η αλλαγή γραμμής.
    l[1]=b+" "
    l[2]=c+" "
    l[3]=d+" "
    l[4]=e+" "
    l[5]=f+" "
#εδώ κατασκευάζω την dd ώστε να έχει στη σειρά τις διατάξεις.
    list(itertools.combinations(l,4))
    aa=[''.join(x) for x in itertools.combinations(l,4)] #φτιάχνω τους συνδυασμούς 4άδων από τα 6 στοιχεία που δίνονται.
#print(aa)
    for i in aa:
        p.append(i.split(" ")) #διαχωρίζω τα στοιχεία των συνδυασμών. 
    for i in p:
        for j in i:
            if(j!=""):
                pp.append(j+" ") #φτιάχνω μία λίστα με τα στοιχεία των συνδυασμών και ένα κενό " " δίπλα ως αντικείμενά της.
    composite_list = [pp[x:x+4] for x in range(0, len(pp),4)] #χωρίζω ανά 4 τα αντικείμενα της pp σε λίστες, τώρα η διαδικασία με τις διατάξεις μπορεί να ξεκινήσει.
    
#print (composite_list)
            
    for i in composite_list:       
        list(itertools.permutations(i,4)) #έχοντας όλους τους συνδυασμούς σε ξεχωριστές λίστες και με τα στοιχεία του καθενός ιδανικά καθορισμένα,
        cc=[''.join(x) for x in itertools.permutations(i,4)] #συμπεριλαμβάνω και τις ισοδύναμες 'μορφές' του κάθε συνδυασμού.
        dd.append(cc) #άρα η dd μοιάζει κάπως έτσι: [['α β γ ','α γ β ','β α γ ', ... ]] 
    print(dd)

    for i in listt:
        bb.append(i.replace("\n"," "))
#print(bb)
    
    k=0
    answer="Unfortunately there was no matching combination found."
    for i in dd:
        for j in i:
            if(j in bb):
                answer="OK " + j
                k=1
                break
        if(k==1):
            break
    return answer

#---------------------------------------------------------------------------------------------------------------|


while(True):
    six=[0,0,0,0,0,0]
    y=1
    x=input("Give the file name or the file's path, \n or type 'stop' to end the programm: \n")
    if(x=="stop" or x=="STOP"):
        break
    else:
        try:
            fin=open(x,"r")
        except IOError:
            print("Could not open the file. Give it another try.\n")
            y=0
        if(y==1):    
            with fin:
                for i in range (6):
                    print("give element ", i+1)
                    temp=input()
                    six[i]=temp
                
                print(six)
                listt=fin.readlines()
                print(check(six[0],six[1],six[2],six[3],six[4],six[5]))
                
print("Exiting. . .\n\n")