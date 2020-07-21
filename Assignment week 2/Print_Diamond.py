#Print the Diamond:

#Draw a pyramid:
rows = int(input("please enter the number of rows in the diamond =  "))
for i in range(rows):
    print(" "*(rows-i-1)+"* "*(i+1))
for j in range(rows-1,0,-1):
    print(" "*(rows-j)+"* "*(j))




