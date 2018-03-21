x=int(raw_input())
y=int(raw_input())
for num in range(x,y):
    c=0
    for i in range(1,y+1):
        if (num%i==0):
            c=c+1
    if(c==2):
	print num
