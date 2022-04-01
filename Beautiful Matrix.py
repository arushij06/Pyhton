# https://codeforces.com/problemset/problem/263/A

mat = []
for i in range(5):
    mat.append(list(map(int,input().split())))
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == 1:
            print((abs(2-i)+abs(2-j)))
            break