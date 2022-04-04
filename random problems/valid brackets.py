# Check whether the provided set of brackets () [] {} is valid or not.
# e.g ({[]}) is valid but ({][}) is not

s = input()
ls = []
j = 0
for i in s:
    if i == '(' or  i == '[' or  i == '{':
        ls.append(i)
    elif i == ')' and len(ls) != 0:
        if ls[-1] == '(':
            ls.pop()
    elif i == ']' and len(ls) != 0:
        if ls[-1] == '[':
            ls.pop()
    elif i == '}' and len(ls) != 0:
        if ls[-1] == '{':
            ls.pop()
    else:
        j+=1
    # if j > 0:
        break
if len(ls) == 0 and j == 0:
    print("Valid")
else:
    print("Invalid")
