# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# From JSON to dictionary
# Sample JSON
userJSON = '{"first_name": "Romain", "last_name": "Testard", "age": 30}'

# Parse to dict
user = json.loads(userJSON)

print(user)
print(user['first_name'])

# FROM dictionary to JSON
car = {'make': 'Ford', 'model': 'Mustand', 'year': 1970}
carJSON = json.dumps(car)
print(carJSON)