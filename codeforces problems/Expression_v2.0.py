"""
Expression_modified - 
Insert signs of operations '+' and '*', and probably brackets between the numbers so that the value of the resulting expression is as large as possible. Let's consider an example: assume that the teacher wrote numbers 1, 2 and 3 on the blackboard. Here are some ways of placing signs and brackets:

    1+2*3=7
    1*(2+3)=5
    1*2*3=6
    (1+2)*3=9 

Note that you can insert operation signs only between a and b, and between b and c, that is, you cannot swap integers. For instance, in the given sample you cannot get expression (1+3)*2.

It's easy to see that the maximum value that you can obtain is 9.

Your task is: given n integers X1, X2...Xn print the maximum value that you can get.

Input:
Input contains n space separated integers X1 X2...Xn.

Output:
Print the maximum value of the expression that you can obtain.

Example:
Input               Output
1 2 3 4             36
"""

def max_exp(ls):
    size = len(ls)
    max_expr = 0
    if size == 0:
        return -1
    elif size == 1:
        return ls[0]
    elif size == 2:
        return max(ls[:1] + ls[1:], ls[:1] * ls[1:])
    else:
        for i in range(1,size):
            max_expr = max(
                max_expr,
                max_exp([max_exp(ls[:i]), max_exp(ls[i:])])
            )
        return max_expr

    # elif size == 3:
    #     return max(
    #         max_exp([max_exp(ls[:1]), max_exp(ls[1:])]), # a +/* (bc)

    #         max_exp([max_exp(ls[:2]), max_exp(ls[2:])]) # (ab) +/* c
    #     )

    # elif size == 4:
    #     return max(
    #         max_exp([max_exp(ls[:1]), max_exp(ls[1:])]) # (a) +/* (bcd)

    #         ,max_exp([max_exp(ls[:2]), max_exp(ls[2:])]) #(ab) +/* (cd)

    #         ,max_exp([max_exp(ls[:3]), max_exp(ls[3:])]) # (abc) +/* d

    #     )
    
num_ele = int(input())
inp_list = list(map(int,input().split()))
print(max_exp(inp_list))

