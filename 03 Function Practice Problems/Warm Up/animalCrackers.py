#
#animalCrackers
#Copyright James Robinson 2018
#All rights reserved
#

'''
ANIMAL CRACKERS: Write a function takes a two-word string
				 and turns True if both words begin with 
				 same letter.
'''

def animal_crackers(text):
	words = (text.lower()).split()

	#print(words)
	if words[0][0] == words[1][0]:
		return(True)
	else:
		return(False)



# Check
print(animal_crackers('Levelheaded Llama'))

# Check
print(animal_crackers('Crazy Kangaroo'))