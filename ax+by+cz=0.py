import math
import matplotlib.pyplot as plt

#This programme is reading a phile which should be like:
"""
(float, float, float) (float, float, float)\n
(float, float, float) (float, float, float)\n
(float, float, float) (float, float, float)\n
                     .
                     .
                     .
(float, float, float) (float, float, float)\n
(float, float, float) (float, float, float)\n
(float, float, float) (float, float, float)\n

"""
#There must be float/int numbers seperated by ',' in each of the brackets, and a '\n' at the end of each line-including the last one.
#==================================================================================================#

def readPoints():
    ans = []
    fin = open(x,"r")
    with fin: 
        temp = fin.readlines()
        for i in temp:
            i = i[:-1]
            temp2 = i.split(" ")
            for j in temp2:
                temp3 = j.split(",")
                temp3[0] = temp3[0][1:]
                temp3[len(temp3) - 1] = temp3[len(temp3) - 1][:-1]
                ans.append(temp3)
        for i in range(0, len(ans), 2):
            print(ans[i], ans[i + 1]) 
        fin.close ()
        return ans

#==================================================================================================#

def findRoots(a, b, c):
    if(c == 0):
        x1 = [1, 0, 0]
        x2 = [0, 1, 0]
    else:
        x1 = [1, 0, -a/c]
        x2 = [0, 1, -b/c]
    #=================================================================#
    y1 = x1
    yy1 = math.sqrt(y1[0]**2 + y1[1]**2 + y1[2]**2)
    v1 = [(1/yy1)*y1[0], (1/yy1)*y1[1], (1/yy1)*y1[2]]
    #=================================================================#
    temp = x2[0]*v1[0] + x2[1]*v1[1] + x2[2]*v1[2]
    y2 = [x2[0] - temp*v1[0], x2[1] - temp*v1[1], x2[2] - temp*v1[2]]
    yy2 = math.sqrt(y2[0]**2 + y2[1]**2 + y2[2]**2)
    v2 = [(1/yy2)*y2[0], (1/yy2)*y2[1], (1/yy2)*y2[2]]
    #=================================================================#
    roots = [v1, v2]
    return roots

#==================================================================================================#

def adjustPoints(points, v):
    #print("v1 =", v[0], "\n\nv2 =", v[1])
    p = []
    for i in range(len(points)):
        temp = [None] * 2
        temp[0] = float(points[i][0])*v[0][0] + float(points[i][0])*v[0][1] + float(points[i][2])*v[0][2]
        temp[1] = float(points[i][0])*v[1][0] + float(points[i][1])*v[1][1] + float(points[i][2])*v[1][2]
        p.append(temp)
    return p

#==================================================================================================#

def display(p, a, b, c):
    strng = "Ax: " + str(a) + "x + " + str(b) + "y + " + str(c) + "z = 0"
    for i in range(0, len(p), 2):
        print(p[i], p[i + 1])
    for i in range (0, len(p), 2):
        plt.plot([p[i][0], p[i + 1][0]], [p[i][1], p[i + 1][1]], 'g-')
    plt.xlabel('v1')
    plt.ylabel('v2')
    plt.title(strng)
    plt.grid(True)
    plt.show()

#==================================================================================================#

while True:
    x = input("Give the file name or the file's path, \n or type 'q' to end the programm: \n")
    if(x == "q" or x == "Q"): break
    try:
        points = readPoints()
        while True:
            print("Give values for a,b,c where a*x + b*y + c*z = 0 || or give 'q' to choose another file")
            try:
                a = input("\nGive a value for a: ")
                if(a.upper() == "Q"): break
                a = float(a)
                b = input("\nGive a value for b: ")
                if(b.upper() == "Q"): break
                b = float(b)
                c = input("\nGive a value for c: ")
                if(c.upper() == "Q"): break
                c = float(c)
                v = findRoots(a, b, c)
                p = adjustPoints(points, v)
                display(p, a, b, c)
            except ValueError: print("\nThere was an error in your input. Please make sure you are giving numbers.\n")
    except IOError:
        print("Could not open the file. Give it another try.\n")
print("Terminating. . .\n\n")