#
#LesserOfTwoEvens
#Copyright James Robinson 2018
#All rights reserved
#

'''
LESSER OF TWO EVENS: Write a function that returns the lesser
					 of two given numbers *if* both numbers 
					 are even, but returns the greater if one 
					 or both numbers are odd.
'''

def lesser_of_two_evens(a,b):
	if (a % 2 == 0) and (b % 2 == 0):
		if a - b <= 0:
			return a
		else:
			return b

	else:
		if a - b <= 0:
			return b
		else:
			return a