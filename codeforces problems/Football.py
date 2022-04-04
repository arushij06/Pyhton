# https://codeforces.com/problemset/problem/96/A

pos = input()
count = 0
for i in range(len(pos)-1):
    if pos[i] == pos[i+1]:
        count += 1
        if count >= 6:
            print( "YES" )
            break
    else:
        count = 0
if count < 6:
    print("NO")