# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes')
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# If you have only one value, leave a trailing coma for it to be a tuple and not just a string
fruits2 = ('Apples',)

# print(fruits, type(fruits2))

# Get value
print(fruits[1])

# Can't change value
# TypeError: 'tuple' object does not support item assignment
# fruits[0] = 'Pears'

# Delete tuple
# del fruits
# print(fruits) Does not exist anymore

# Get length
print(len(fruits))



# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Remove from set
fruits_set.remove('Grape')

# Cleat set
fruits_set.clear()

# Delete
del fruits_set

print(fruits_set)