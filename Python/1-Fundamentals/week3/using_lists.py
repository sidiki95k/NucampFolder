states = ["washington", "Oregon", "California"]
'''
print(states[-1])
print(states[-2])
print(states[-3])
'''

# Arizona has taken the place of California as the third list item
states[2] = "Arizona"
print(states)

#The length of a list is the total number of items in that list
print(len(states))

#The append() method adds an item to the end of a list
states.append("New York")
print(states)

#Used with an empty argument list, it will remove ("pop" off) the last item from the list
states.pop()
print(states)

states.pop(1)
print(states)



