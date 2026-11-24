a = int(input("Enter your age : "))

#if , elif and else ladder 

if(a>18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("Invalid age")

elif(a==0):
    print("0 is not a valid age")

else:
    print("you are below the age of consent")


print("End of the program")
