from typing import final


age = 32
age_as_str = str(age)

print("You are " + age_as_str)
print(f'You are {age}')

name = 'Jose'
greeting = f'How are you {name}'
print(greeting)

name ='Bob'
print(greeting) #still have old value: how are you Jose

name = 'Jose'
final_greeting = "how are you, {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)
bob_greeting = final_greeting.format('Bob')
print(bob_greeting)