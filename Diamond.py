n=int(input())
g=1
m=n
for i in range(n):
	for j in range(m):
		print("*",end="")
	for j in range(g):
		print(" ",end="")
	g+=2
	for j in range(m):
		print("*",end="")
	m-=1
	print()
m+=2
g-=4
for i in range(n-1):
	for j in range(m):
		print("*",end="")
	for j in range(g):
		print(" ",end="")
	g-=2
	for j in range(m):
		print("*",end="")
	m+=1
	print()	
