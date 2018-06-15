#
#oldMacDonald
#Copyright James Robinson 2018
#All rights reserved
#

'''
OLD MACDONALD: Write a function that capitalizes the first and 
			   fourth letters of a name
'''

def old_macdonald(name):
	return name[:3].capitalize() + name[3:].capitalize()

# Check
print(old_macdonald('macdonald'))
