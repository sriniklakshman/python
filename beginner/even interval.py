n=int(raw_input( ))
m=int(raw_input( ))
if(n,m<=100000):
	for i in range(n+1,m):
		if(i%2==0):
			print(i)
