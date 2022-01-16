"""
    Dictionaries cannot have duplicate keys
"""

friends = {
    'Rolf':24, 
    'Adam':25,
    'Anne':26
}
friends['Bob'] = 27 #add
friends['Rolf'] = 20 #update

print(friends['Rolf'])
print(friends)

friends = (
    {'name': 'Rolf', 'age': 24},
    {'name': 'Adam', 'age': 25},
    {'name': 'Anne', 'age': 26}
)

print(friends)
print(f'first Element: {friends[0]["name"]}')

friends = [("Rolf",24), ("Adam", 25), ("Anne", 26)]
friend_ages = dict(friends)
print(friend_ages)