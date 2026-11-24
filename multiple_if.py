a = int(input("Enter your age : "))

#if statement no:1
if(a%2==0):
    print("age is even")
#End of if statement no 1

#if statement no:2
if(a%2==1):  #you can also use else:print("age is odd")
    print("age is odd")
#End of if statement no 2


#if statement no:3
if(a>18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("Invalid age")

elif(a==0):
    print("0 is not a valid age")

else:
    print("you are below the age of consent")
#End of if statement no 3


print("End of the program")
