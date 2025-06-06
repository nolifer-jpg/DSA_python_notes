Recursion:
	divide and conquer, decrease and conquer
	reduce the problem into simpler version
	when reduce to a version we can solve directly exit the iteration
	
	def fact(n):
		if n ==1:
		  return 1
		else:
		  return n*fact(n-1)
	
	print(fact(4))

	each recursive call to a function creates its own scope 
	recursion is easy to understand

dicts are mutable