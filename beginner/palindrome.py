x=raw_input()
temp=x
a=0
while(temp!=0):
	a=a*10+int(temp%10)
	temp=(temp/10)
if(a==x):
	print("palindrome")
else:
	print("no")
