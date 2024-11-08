
def max_subarr_sum(arr):
    max_sum=float('-inf')
    n=len(arr)

    for start in range(n):
        for end in range(start,n):
            curr_sum=sum(arr[start:end+1])
            max_sum=max(max_sum,curr_sum)

    return max_sum


user_input=input("enter elements : ")
arr=list(map(int,user_input.split()))

result=max_subarr_sum(arr)
print("Max-sum : ", result)
