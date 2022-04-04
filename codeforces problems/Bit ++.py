# https://codeforces.com/problemset/problem/282/A

n = int(input())
ls = []
x = 0
for i in range(n):
    ls.append(input())
    if ls[i].find('+') >=0:
        x += 1
    if ls[i].find('-') >=0:
        x -= 1
print(x)