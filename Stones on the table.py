# https://codeforces.com/problemset/problem/266/A

n = int(input())
color = input()
if 1<=n<=50 and len(color) == n:
    count = 0
    for i in range(n-1):
        if color[i] == color[i+1]:
            count += 1
    print(count)