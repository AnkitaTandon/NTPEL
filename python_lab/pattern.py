'''
Q2: Write a program to generate the following pattern, using nested for loop.

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*

'''

for i in range(1,6):
	for j in range(i):
		print(" *",end="")
	print("\n",end='')
for i in range(4,0,-1):
	for j in range(i):
		print(" *",end="")
	print("\n",end='')
