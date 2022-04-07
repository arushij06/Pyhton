"""
Kefa and First Steps - https://codeforces.com/problemset/problem/580/A

Kefa decided to make some money doing business on the Internet for exactly n days. He knows that on the i-th day (1 ≤ i ≤ n) he makes ai money. Kefa loves progress, that's why he wants to know the length of the maximum non-decreasing subsegment in sequence ai. Let us remind you that the subsegment of the sequence is its continuous fragment. A subsegment of numbers is called non-decreasing if all numbers in it follow in the non-decreasing order.

Help Kefa cope with this task!
Input

The first line contains integer n (1 ≤ n ≤ 105).

The second line contains n integers a1,  a2,  ...,  an (1 ≤ ai ≤ 109).
Output

Print a single integer — the length of the maximum non-decreasing subsegment of sequence a.

Examples
Input                   Output
6                       3  
2 2 1 3 4 1

"""

def maxSubsegmentlength(sequence):
    count = 1
    max_count = 1
    for num in range(len(sequence) - 1): 
        if sequence[num] <= sequence[num + 1]:
            count += 1
        else:
            count = 1
        if max_count < count:
            max_count = count
    return max_count

total_integers = int(input())
seq = list(map(int,input().split()))
print(maxSubsegmentlength(seq))
