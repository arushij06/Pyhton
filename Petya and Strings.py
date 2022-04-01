# https://codeforces.com/problemset/problem/112/A

s1 = input().lower()
s2 = input().lower()
if 1<=len(s1)<=100 and 1<=len(s2)<=100:
    count = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            pass
        elif s1[i] < s2[i]:
            count -= 1
            break
        else:
            count += 1
            break
    print(count)