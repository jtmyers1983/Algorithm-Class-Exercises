#	Masters Theorum is used to determine the running time(tight bound theta)
#	of a large class of recursive algorithims

# 	T(n) is the running time when the input size is n

#	T(n) = n^d	 + a*T(n/b)

'''
In this abstract equation: 
- how many recursive calls? = a
- Input ize of each recursive call? = n/b
- processing time? = Theta(n^d)

!!! To find out the complexity of T(n), we compare d and log_b(a)!!!!
We have 3 cases:
(1) d > log_b(a), T(n) is in Theta(n^d)
(2) d < log_b(a), T(n) is in Theta(n^(log_b(a)))
(3) d = log_b(a), T(n) is in Theta(n^d * log(n))

'''

def foo(L):					#	T(n) = ?
	if L == []:				#	1
		return 1			#	
	A = L[0:len(L)//2]		#	n/2
	return 1 + foo(A)		#	1 + T(n/2)

'''
n is length l
foo has 1 recursive call? 
input size of each recursive call is n/2. 
what is the running time equation of foo? 
T(n) = 3 + n/2 + T(n/2)
We can simplify this as: T(n) = n/2 + T(n/2)
a= 1	
b= 2
d= 1

We compare 1 and log_2(1) = 0
so T(n) is in Theta(n)

'''