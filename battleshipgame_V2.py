import numpy as np
import random

shipboard = np.array([['a','b','c','d'],['e','f','g','h'],['i','j','k','l']])

#computer shoots at your_shipboard
your_shipboard_alphabet =  np.array([['a','b','c','d'],['e','f','g','h'],['i','j','k','l']])

#ships at which you aim
shipboard2 = np.array([[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]])

#your_shipboard = np.array([[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)],[random.randint(0,1),random.randint(0,1),random.randint(0,1),random.randint(0,1)]])
your_shipboard =  np.array([['a','b','c','d'],['e','f','g','h'],['i','j','k','l']])
#your_shipboard =  np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])

ships = np.where(shipboard2 == 1)
possible_computer_choices = ['a','b','c','d','e','f','g','h','i','j','k','l']





#input your ships
ship = input("Where would you like to place your first ship?" )
for coord in np.nditer(your_shipboard, op_flags=['readwrite']):
    if coord == ship:
        coord[...] = 1
ship = input("Where would you like to place your second ship?" )
for coord in np.nditer(your_shipboard, op_flags=['readwrite']):
    if coord == ship:
        coord[...] = 1
ship = input("Where would you like to place your third ship?" )
for coord in np.nditer(your_shipboard, op_flags=['readwrite']):
    if coord == ship:
        coord[...] = 1
ship = input("Where would you like to place your fourth ship?" )
for coord in np.nditer(your_shipboard, op_flags=['readwrite']):
    if coord == ship:
        coord[...] = 1
ship = input("Where would you like to place your fifth ship?" )
for coord in np.nditer(your_shipboard, op_flags=['readwrite']):
    if coord == ship:
        coord[...] = 1

for coord in np.nditer(your_shipboard, op_flags=['readwrite']):
    if coord != '1':
        coord[...] = 0

your_ships = np.where(your_shipboard == '1')
coordinates_of_ships= list(zip(ships[0], ships[1]))
your_coordinates_of_ships = list(zip(your_ships[0], your_ships[1]))
game_wins = 0
game_losses = 0
playing = True
print('There are:', len(coordinates_of_ships), 'ships in the enemy fleet')
print('There are:', len(your_coordinates_of_ships),'ships in your fleet')
print("And the locations of your ships are the 1's here, don't tell anyone!:")
print(your_shipboard)

while playing == True:

    print('Your board looks like:')
    print(your_shipboard_alphabet)
    print("Your opponent's board looks like:")
    print(shipboard)
    selection = input("Where would you like to fire your missile? ")
    where_is_this_coordinate = np.where(shipboard == selection)
    coords = list(zip(where_is_this_coordinate[0], where_is_this_coordinate[1]))
    misses = 0

    for coord in coords:
        print(coord)

    for coord in coords:

        if coord in coordinates_of_ships:
            for value in np.nditer(shipboard, op_flags=['readwrite']):
                if value == selection:
                    print("You hit one!")
                    value[...] = 'o'

        else:
            for value in np.nditer(shipboard, op_flags=['readwrite']):
                if value == selection:
                    print("No boat!")
                    value[...] = 'x'
                    misses += 1

        list_of_os = np.where(shipboard == 'o')
        coords_of_os = list(zip(list_of_os[0],list_of_os[1]))

        if coordinates_of_ships == coords_of_os:
            print("You've destroyed the enemy fleet! You win!")
            game_wins += 1
            playing = False


    comp_choice =  random.choice(possible_computer_choices)
    possible_computer_choices.remove(comp_choice)
    where_is_this_coordinate = np.where(your_shipboard_alphabet == comp_choice)
    coords = list(zip(where_is_this_coordinate[0], where_is_this_coordinate[1]))

    for coord in coords:

        if coord in your_coordinates_of_ships:
            for value in np.nditer(your_shipboard_alphabet, op_flags=['readwrite']):
                if value == comp_choice:
                    print("The computer hit you!")
                    value[...] = 'o'

        else:
            for value in np.nditer(your_shipboard_alphabet, op_flags=['readwrite']):
                if value == comp_choice:
                    print("The computer missed!")
                    value[...] = 'x'

        list_of_os = np.where(your_shipboard_alphabet == 'o')
        coords_of_os = list(zip(list_of_os[0],list_of_os[1]))


        if your_coordinates_of_ships == coords_of_os:
            print("You lost, your fleet has been destroyed!")
            game_losses += 1
            playing = False

def statistics ():
    '''Finds statistics about the player's journey'''
    print("wins: ", game_wins)
    print("losses: ", game_losses)
def clear_stats():
    '''Resets a player's statistics to 0'''
    global game_wins
    global game_losses
    game_wins = 0
    game_losses = 0
statistics()