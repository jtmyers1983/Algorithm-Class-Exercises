'''
Making change
Given n coins: c0, c1,...,c_n-1
Given d amount to make change using these coins
Can we make change for d using these coins?>

Ex. coins = [2,5], d = 9. True 9 = 2 + 2 + 5
Ex. coins = [5,9], d = 17. False
'''

def change(coins, d):
	if d < 0:
		return False
	if d == 0:
		return True
	for c in coins:
		if change(coins, d-c) == True:
			return True
	return False										


print(change([2,5], 9))
print(change([5,9], 17))
print(change([11,23], 139))

'''
coins = [11,23,10]
d = 139

we can make change for 139 if and only if:
	- we can make change for 128 or
	- we can make change for 116 or
	- we can make change for 129
why? because the first coin is either 11, or 23, or 10.
This strategy/ reasoning considers "all possibilities"

Compare this vs a 'Greedy' strategy. Take the largest coin(23) out of 139.



change([11,23,10]) = change([11,23,10], 128) or change([11,23,10], 116) or change([11,23,10], 129)
'''

#Cache this. Cache just means worry about input and output, no need to worry about logic of program.
Table = {}	# key; is (input) ; Value = ouput
			#so Key is = (coins, d) | Value = change(coins, d)	
def change(coins, d):
	if d < 0:
		return False
	if d == 0:
		return True
	for c in coins:
		if change(coins, d-c) == True:
			return True
	return False										


print(change([2,5], 9))
print(change([5,9], 17))
print(change([11,23], 139))



