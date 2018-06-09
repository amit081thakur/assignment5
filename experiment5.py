Python 3.7.0b5 (v3.7.0b5:abb8802389, May 31 2018, 01:54:01) [MSC v.1913 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information:
>>>
>>>        
>>> #Q.1- Take an input year from user and decide whether it is a leap year or not.
>>>
>>>
>>> list=[ 1980,1984,1986,1988,1991,1996,2000,2004]
>>> print(list)
[1980, 1984, 1986, 1988, 1991, 1996, 2000, 2004]
>>> x=0
>>> for x in list:
	print(x)
	if x%4==0:
		if x%100==0:
			if x%400==0:
				print("leap year:" ,x)
			else:
				print("not a leap year:",x)
		else:
			print("leap year:",x)
	else:
		print(" not a leap year:",x)

		
1980
leap year: 1980
1984
leap year: 1984
1986
 not a leap year: 1986
1988
leap year: 1988
1991
 not a leap year: 1991
1996
leap year: 1996
2000
leap year: 2000
2004
leap year: 2004
>>>
>>>
>>>
>>> #Q.2- Take length and breadth input from user and check whether the dimensions
>>> #     are of square or rectangle. 
>>>
>>>
>>> def determine():
	for x in range(2):
		l= input("\nlength=")
		b= input("breadth=")
		if l==b:
			print(" these dimension are of square:",(l,b))
		else:
			print("these dimension are of rectangle:", (l,b))

			
>>> determine()

length=56
breadth=67
these dimension are of rectangle: ('56', '67')

length=56
breadth=56
 these dimension are of square: ('56', '56')
>>>
>>>
>>>
>>> #Q.3- Take the input age of 3 people and determine oldest and youngest among them.
>>>
>>> 
>>> x=45
>>> y=34
>>> z=56
>>> if x>y:
	if x>z:
		print("x is greater")
	else:
		print("z is greater")
else:
	print("y is greater")

	
z is greater
>>>
>>>
>>>
>>>
>>> #Q.4- Write an if statement that lets a competitor know which of these prizes
>>> #they won based on the number of points they scored.
>>>
>>> def awards():
	for x in range(7):
		point = int(input("\n tell your points:"))
		if 0 <= point <= 50:
			print("Sorry! No prize this time.")
		else:
			if 51 <= point <= 150:
				print("Congratulations! You won wooden dog")
			else:
				if 180 <= point <= 200:
					print("Congratulations! You won chocolates")
				else:
					print(" invalid points")

					
>>> awards()

 tell your points:45
Sorry! No prize this time.

 tell your points:78
Congratulations! You won wooden dog

 tell your points:89
Congratulations! You won wooden dog

 tell your points:200
Congratulations! You won chocolates

 tell your points:123
Congratulations! You won wooden dog

 tell your points:78
Congratulations! You won wooden dog

 tell your points:789
 invalid points

>>>
>>>
>>>
>>>
>>>#Q.5- A shop will give discount of 10% if the cost
>>>#of purchased quantity is more than 1000.Ask user
>>>#for quantity Suppose, one unit will cost 100. Judge
>>>#and print total cost for user.
>>>
>>>
>>> def amount():
	for x in range(5):
		pay = int()
		cost = int()
		quantity = int(input("\nenter the quantity:"))
		cost = 100 * quantity
		if cost > 1000:
			pay = cost - 0.10*cost
			print("you have to pay:",pay)
		else:
			print("you have to pay:",cost)

			
>>> amount()

enter the quantity:23
you have to pay: 2070.0

enter the quantity:45
you have to pay: 4050.0

enter the quantity:2
you have to pay: 200

enter the quantity:5
you have to pay: 500

enter the quantity:9
you have to pay: 900

