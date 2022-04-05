"""
Find the sum of contiguous subarray within a one-dimensional array of numbers that has the largest sum.

Input:                    Output:
-2 -3 4 -1 -2 1 5 -3      7
"""

def maxSubArraySum(ls):
    max_sum = 0
    size = len(ls)
    sub_arr = []
    for i in range(size):
        for j in range(i+1 ,size+1):
            if max_sum < sum(ls[i:j]):
                max_sum = sum(ls[i:j])
                sub_arr = ls[i:j]
    return max_sum, sub_arr


inp_list = list(map(int,input().split()))
print(maxSubArraySum(inp_list))