# The stock span problem

s = list(map(int, input().split(",")))
ls = []
for i in range(len(s)):
    counter = 1
    for j in range(i,0,-1):
        if s[i] > s[j-1]:
            counter += 1
        else:
            break
    ls.append(counter)
print(ls)