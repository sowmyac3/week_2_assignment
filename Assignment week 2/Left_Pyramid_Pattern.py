
#Print a left half pyramid pattern with whatever symbol you want

#Defining Variables
rows = 4
num = 2*rows - 2


#Main Code:
for i in range(0,rows):
    for j in range(0,num):
        print(end=" ")
    num = num - 2

    for j in range(0,i+1):
        print("*",end = " ")
    #prints a new line
    print("\r")
        

        
