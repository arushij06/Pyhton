# https://codeforces.com/problemset/problem/1/A

size = input()
a = list(map(int, size.split()))
    
rect_len = a[0]
rect_br = a[1]
sq_side = a[2]
l = rect_len//sq_side
if rect_len % sq_side != 0:
    l += 1

b = rect_br // sq_side
if rect_br % sq_side != 0:
    b += 1
    
print(l*b)