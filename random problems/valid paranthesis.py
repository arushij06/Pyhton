# check whether given set of parathesis form a valid expression
# eg. ((())()) is valid but )()() is not

s = input()
n=0
for c in s:
	if c=='(':
		n+=1 
	elif c==')':
		n-=1
	if n<0:
		break;
if n==0:
	print("Valid")
else:
	print("Invalid")