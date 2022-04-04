"""
Expression - https://codeforces.com/problemset/problem/479/A

Petya studies in a school and he adores Maths. His class has been studying arithmetic expressions. On the last class the teacher wrote three positive integers a, b, c on the blackboard. The task was to insert signs of operations '+' and '*', and probably brackets between the numbers so that the value of the resulting expression is as large as possible. Let's consider an example: assume that the teacher wrote numbers 1, 2 and 3 on the blackboard. Here are some ways of placing signs and brackets:

    1+2*3=7
    1*(2+3)=5
    1*2*3=6
    (1+2)*3=9 

Note that you can insert operation signs only between a and b, and between b and c, that is, you cannot swap integers. For instance, in the given sample you cannot get expression (1+3)*2.

It's easy to see that the maximum value that you can obtain is 9.

Your task is: given a, b and c print the maximum value that you can get.

Input:
The input contains three integers a, b and c, each on a single line (1 ≤ a, b, c ≤ 10).

Output:
Print the maximum value of the expression that you can obtain.

Example:
Input               Output
1                   9
2
3
"""

def max_exp(ls):
    size = len(ls)
    if size == 0:
        return 0
    elif size == 1:
        return ls
    elif size == 2:
        return max(ls[0]+ls[1], ls[0]*ls[1])
    else:
        return max(
            ls[0] + max_exp(ls[1:]),
            
            ls[0] * max_exp(ls[1:]),

            max_exp(ls[0:2]) + ls[2],

            max_exp(ls[0:2]) * ls[2]
        )
    
inp_list = []
first_num = inp_list.append(int(input()))
second_num = inp_list.append(int(input()))
third_num = inp_list.append(int(input()))
fourth_num = inp_list.append(int(input()))
print(max_exp(inp_list))

