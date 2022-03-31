#  https://codeforces.com/problemset/problem/71/A

n = int(input())
input_words = []
for i in range(n):
    input_words.append(input())
for ele in input_words:
    if len(ele) > 10:
        print(ele[0] + str(len(ele)-2) + ele[-1])
    else:
        print(ele)