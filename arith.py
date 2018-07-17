print("1. Arithmetic")
print("2. Comparision")

c=int(input("Enter your choice (1,2 or 3) "))

if(c==1):
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	o=int(input("Enter the operation(1,2,3 or 4) "))
	a=int(input("Enter first number"))
	b=int(input("Enter second number"))
	if(o==1):
		res=a+b
		print("Addition of the number: ",res)
	elif(o==2):
		res=a-b
		print("Subtraction of the number: ",res)
	elif(o==3):
		res=a*b
		print("Multiplication of the number: ",res)
	else:
		res=a//b
		print("Division of the number: ",res)
elif(c==2):
	a=int(input("Enter first number"))
	b=int(input("Enter second number"))
	if(a>b):
		print(a," is greater than ",b)
	elif(a<b):
		print(a," is less than ",b)
	elif(a==b):
		print(a," is equal to ",b)
else:
	print("Invalid input")	


