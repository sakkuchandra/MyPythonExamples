person = {"name": "Jessa", 'country': "USA"}

# Adding 2 new keys at once
# pass new keys as dict
person.update({"weight": 50, "height": 6})
# print the updated dictionary
print(person)
# output {'name': 'Jessa', 'country': 'USA', 'weight': 50, 'height': 6}

# pass new keys as as list of tuple
person.update([("city", "Texas"), ("company", "Google",)])
# print the updated dictionary
print(person)
# output {'name': 'Jessa', 'country': 'USA', 'weight': 50, 'height': 6, 'city': 'Texas', 'company': 'Google'}




     










