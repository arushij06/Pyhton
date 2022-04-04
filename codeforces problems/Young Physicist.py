# https://codeforces.com/problemset/problem/69/A

n = int(input())
ls=[]
for rows in range(n):
    ls.append(list(map(int,input().split())))
x,y,z = 0,0,0
for i in range(n):
    x += (ls[i][0])
    y += (ls[i][1])
    z += (ls[i][2])
if x==0 and y==0 and z ==0:
    print("YES")
else:
    print("NO")