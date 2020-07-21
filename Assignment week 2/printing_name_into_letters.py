#Display a word by letter

message = str(input("Enter a string message: "))
lenght = len(message)

for i in range(lenght):
    for j in range(i+1):
        print(message[j], end="")
    print("\r")
        
