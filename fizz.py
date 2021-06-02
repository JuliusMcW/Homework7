
def buzz():
	x=1
	z="1"
	y=" "
	while x<=100:
		z=str(x)
		if x%3==0:
			z="Fizz"
			if x%5==0:
				z=z+"Buzz"	
		elif x%5==0:
			z="Buzz"		
		y=y+z+' '
		x=x+1
	print(y)	
