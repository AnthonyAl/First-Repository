while(True):
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
                v2=fin.readlines()
                v3=[]
                v5=[]
                z=0 #elegxos pou den afinei ta sunexomena kena na metrane sthn v4.
                v4=" "
                for i in v2:
                    for j in i:
                        if(j==" " or j=="\t" or j=="\n" or j=="." or j=="," or j=="?" or j==";" or j==":" or j=='"' or j=="<" or j==">" or j=="!" and z!=0):
                            l=len(v4)
                            if(l>4):
                                v6=v4[2:]
                                v7=v4[1]
                                v8=v6+v7+"ay"
                                v5.append(v8)
                            v3.append(v4[1:])
                            v4=" "
                            z=0
                        elif(j==v2[-1][-1]):
                            v4+=v2[-1][-1]
                            l=len(v4)
                            if(l>4):
                                v6=v4[2:]
                                v7=v4[1]
                                v8=v6+v7+"ay"
                                v5.append(v8)
                            v3.append(v4[1:])
                        elif(j!=" " and j!="\t" and j!="\n" and j!="." and j!="," and j!="?" and j!=";" and j!=":" and j!='"' and j!="<" and j!=">" and j!="!"):
                            z=1
                            v4=v4+j
                print("Oi le3eis tou arxeiou:\n")
                for i in v3:
                    if(len(i)>0):
                        print(i)
                print("\n")
                print("Oi le3eis tou arxeiou meta thn metatroph:\n")
                for i in v5:
                    if(len(i)>0):
                        print(i)
                fin.close ()

print("Exiting. . .\n\n")
