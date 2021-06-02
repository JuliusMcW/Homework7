def buzz(a):
	x=1
	z="1"
	y="Print "
	while x<=a:
		z=str(x)
		if x%3==0:
			z="fizz"			
		y=y+z+' '
		x=x+1
	return y		
