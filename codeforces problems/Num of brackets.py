# Print number of open and closed brackets in given input string.

s = input()
num_open = 0
num_closed = 0
for i in s:
    if i == '(':
        num_open += 1
    elif i == ')':
        num_closed += 1
print("Open brackets : ",num_open)
print("Closed brackets : ", num_closed)
