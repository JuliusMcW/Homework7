

def leapy(a):
	if a%4==0:
		if a%400:
			print('Yes,', a,   'is a leap year')
			return True
		else:
			print('No,', a,   'is not a leap year')
			return False


	else:
		print('No,', a,   'is not a leap year')
		return False


