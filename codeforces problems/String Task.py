# https://codeforces.com/problemset/problem/118/A

s1 = input().lower()
s2 = ""
for ch in s1:
    if ch in ('a','e','i','o','u','y'):
        s2+=""
    else:
        s2 = s2 + "." + ch
print(s2)