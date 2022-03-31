# https://codeforces.com/problemset/problem/158/A

ls = list(map(int,(input().split())))
scores = list(map(int,input().split()))
count = 0
for i in range(len(scores)):
    if scores[i] > 0 and scores[i] >= scores[ls[1]-1]:
        count += 1
print(count)