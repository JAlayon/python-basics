art_friends = {'Rolf', 'Anne'}
science_friends = {'Jen', 'Charlie'}

art_friends.add('Jen')
print(f'Art friends: {art_friends}')
print(f'Science Friends: {science_friends}')

#Advance set operations
art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)
not_in_both = art_friends.symmetric_difference(science_friends)
print(f'Art but not science: {art_but_not_science}')
print(f'Science but not art: {science_but_not_art}')
print(f'Not in Both: {not_in_both}')

art_and_science = art_friends.intersection(science_friends)
print(f'Art and Science: {art_and_science}')

all_friends = art_friends.union(science_friends) #without repeating
print(f'All friends {all_friends}')