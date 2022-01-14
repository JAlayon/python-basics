age = int(input('Enter your age: '))
can_learn_programming = age > 0 and age < 100

print(f'You can learn programming_ {can_learn_programming}')

age = int(input('Enter your age: '))
usually_not_working = age < 18 or age > 65
print(f'At {age}, you usually not working: {usually_not_working}')


print(bool(35)) #True
print(bool('hello')) #True
print(bool(0)) #False
print(bool('')) #False