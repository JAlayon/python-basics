friends = ['Rolf', 'Bob', 'Anne']

print(friends[0])
print(friends[1])
print(friends[2])

print(f'Length: {len(friends)}' )

friends = [['Rolf',24], ['Bob', 25], ['Anne',26]]
print(friends[0][0]) #Rolf
print(friends[0][1]) #24

friends.append('Jen')
print(friends)