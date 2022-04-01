# https://codeforces.com/problemset/problem/546/A

ls = list(map(int,input().split()))
to_pay = 0
for i in range(1,ls[2]+1):
    to_pay += (i*ls[0])
if to_pay > ls[1]:
    print(to_pay - ls[1])
else:
    print(0)