# Given N elements in a list, count the no of elements having atleast 1 greater than itself
# list = 2 5 1 4 8 0 8 1 3 8

def greatestEle(arr):
    n=len(arr)
    max_ele=arr[0]

    for i in range(1,n):
        if arr[i]>max_ele:
            max_ele=arr[i]
        
    cnt=0
    for i in range(1,n):
        if arr[i]==max_ele:
            cnt+=1

    return n-cnt;



user_input=input("Enter elements : ")

arr=list(map(int,user_input.split()))

print("Greatest element : " ,greatestEle(arr))
 

