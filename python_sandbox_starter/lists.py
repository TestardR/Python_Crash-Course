# A List is a collection which is ordered and changeable. Allows duplicate members.

#  Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#  Use a constructor
numbers2 = list((1, 2, 3, 4, 5))

# print(numbers, numbers2)

#  Get a value
print(fruits[1])

# Change value
fruits[0] = 'Blueberries'

# Get a length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove form list
fruits.remove('Grapes')

# Insert into specific position
fruits.insert(3, 'Banana')

# Remove with pop (specific position)
fruits.pop(3)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

print(fruits)
