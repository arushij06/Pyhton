# https://codeforces.com/problemset/problem/231/A

questions = int(input())
ls = [input().split() for i in range(questions)]
count = 0
for i in range(len(ls)):
    sum = 0
    for j in range(len(ls[i])):
        sum += int(ls[i][j])
    if sum >= 2:
        count += 1
print(count)