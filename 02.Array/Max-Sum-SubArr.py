# Given an array of size N. find and return the max sum of any sub array  i/p => -2 3 5 -1 5 10 7

# brute force approach

def max_subarr_sum(arr):
    max_sum=float('-inf')
    n=len(arr)

    # loop through each start point
    for start in range(n):
        # loop through each possible ending point for the current starting pointing
        for end in range(start,n):
            # calculate sum of the subarray from start to end
            curr_sum=sum(arr[start:end+1]) # slicing creates a subarrauy
            # update maxSum
            max_sum=max(max_sum,curr_sum)

    return max_sum


# optimized approach with kadane's algo

def max_subArr_sum(arr):
    cur_sum=arr[0]
    max_sum=arr[0]

    for i in range(1,len(arr)):
        cur_sum=max(arr[i],cur_sum+arr[i])
        max_sum=max(cur_sum,max_sum)
    return max_sum    

# Get user input

user_input=input("Enter arr elements : ")
arr=list(map(int,user_input.split()))


# call the function
print("Max subarray sum : ", max_subArr_sum(arr))