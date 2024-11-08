# age=int(input("Enter age : " ))

# if(age>18):
#     print("You can vote in Lok sabha elecion")
# else:
#     print("You cannot vote in this election")   

# print("End of the election")     
    

# a={1,2,3,5,87}

a="shubham"

# for i in a:
#     print(i)

# for i in range(1,6,2):
#     print(i)

n=int(input("Enter N : " ))
# for i in range(1, n+1):
#     print(" "* (n-i),end="")
#     print("*"* (2*i-1),end="")
#     print(" ")

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*" * n,end="")
    else:
        print("*", end="")
        print(" "*(n-2),end="")
        print("*",end="") 
    print(" ")       
