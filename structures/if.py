friend = 'Rolf'
user_name = input('Enter your name: ')

if user_name == friend:
    print('Hello Friend')
else:
    print('Hello Stranger')


friends = ['Rolf', 'Bob', 'Anne']
family = ['Jen', 'Charlie']

user_name = input('Enter your name: ')

if user_name in friends:
    print('Hello Friend')
elif user_name in family:
    print('Hello Family')
else:
    print('I dont know you')