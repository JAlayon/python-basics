lottery_numbers = {13, 21, 22, 5, 8}


"""
A player looks like this:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

Define a list with two players (you can come up with their names and numbers).
"""

players = [
    {
        'name':'Jair',
        'numbers':{1,4,9,8}
    }, 
    {
        'name':'Mariana',
        'numbers':{2,9,10}
    }
]

"""
For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
Then construct a string and print it out.

Remember: the string must contain the player's name and the amount of numbers they got right!
"""

total_player_1 = len(lottery_numbers.intersection(players[0]['numbers']))
total_player_2 = len(lottery_numbers.intersection(players[1]['numbers']))

print(f'Player {players[0]["name"]} got {total_player_1} numbers right.')
print(f'Player {players[1]["name"]} got {total_player_2} numbers right.')
