def permutations(string): 
	if len(string) < 2: 
		return 0 

	print permutations(string[:]) 

	return string

def fibonacci(n):
	if (n==0) or (n==1): 
		return n 
	else:
		print fibonacci(n-1) * fibonacci(n-2)
		return fibonacci(n-1) * fibonacci(n-2)


def recursice(string,no):
	if no == 0: 
		return 1
	print "%s - %s" % (string,no)
	recursice(string, no-1/12)

def divisorPair(yes):
	result = 0
	for i in range(len(yes)-1):
		j = i+1 
		while j < len(yes)-1:
			if (yes[i] % yes[j] == 0) or (yes[j] % yes[i] == 0): 
				result +=1 
			j=j+1
	return result 

print divisorPair([1,2,4])



