# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:       Alex Keener, Sean Kelly, Andrew Kinnick
# Section:     515
# Assignment:  Lab 13 - Activity 1
# Date:        20 11  2020

import csv
from random import randint
import math


def account_login(account_name):
    """This function receives input of an account name(string) and will find the matching information file to the
    account name. It will return the name of this file. If the account name is equal to 'none', a new user and file
    will be created."""
    if account_name == 'none':  # calls create_user() function to create a new profile
        account_name = create_user()
    else:
        account_name = account_name + '.csv'
    file_name = account_name
    return file_name


def create_user():
    """This function will create a new profile using a user chosen name and assign that user a random pokemon. It will
    also create a new file using this chosen username and return the shared name of the file and profile(String)."""

    profile_name = input('Please enter the username you would like: ') + '.csv'

    # assigns a random pokemon to the new user
    pokemon = open('PokeList_v3.csv', 'r', )
    pokemon_reader = csv.reader(pokemon, delimiter=',')
    available_pokemon = list(pokemon_reader)
    available_pokemon.pop(0)
    poke_num = randint(0, 150)
    poke_name = available_pokemon[poke_num][1]
    level = randint(0, 30)
    cp = randint(int(available_pokemon[poke_num][2]), int(available_pokemon[poke_num][3]))

    # writes this new pokemon into the user's file
    new_account = open('{}'.format(profile_name), 'w+',newline='')  # creates the user file for the new user
    poke_writer = csv.writer(new_account, delimiter=',')
    pokemon = [poke_name, level, cp]
    poke_writer.writerow(pokemon)
    new_account.close()

    return profile_name


def account_switch(account_name):
    """This function receives input of an account name(string). The function will then return the file to be used in
    association with this account name(string)."""
    account_name = account_name + '.csv'
    return account_name


def display_main_menu():
    """This function prints the main menu to the user and will return the value of the selection the user
    chooses(integer)."""
    print('-' * 10 + ' Main Menu ' + '-' * 10)
    print('1. View Current Pokemon')
    print('2. Catch Pokemon')
    print('3. Battle')
    print('4. Switch User')
    print('5. Exit Game')
    choice = int(input('Enter the number of the selection you would like: '))
    return choice


def catch_pokemon(candy):
    """This function receives the argument of candy(integer).Then, this function will output a math problem for the user
     to solve. If the user solves it, the function will add a random pokemon that they have caught to their profile file
      and add 1 candy to the user's amount. The function will then return the updated candy amount (integer)."""

    caught = math_problem_generator()
    # adds the pokemon to the file if the user successfully catches a pokemon
    if caught:
        poke_name, poke_level, poke_cp = random_pokemon(caught)
        print('Congrats! You\'ve caught a level {} {}. You can view its full stats in the pokemon selector menu.'
              .format(poke_level, poke_name))

        with open('{}'.format(fileID), 'a', newline='') as pokeFile:
            poke_writer = csv.writer(pokeFile, delimiter=',')
            pokemon = [poke_name, poke_level, poke_cp]
            poke_writer.writerow(pokemon)
        # sometimes a new user will receive a type error here the first time they try to catch a pokemon.
        # This rectifies that issue
        try:
            candy = candy + 1
        except TypeError:
            candy = 5
            candy += 1

        return candy


def random_pokemon(catch):
    """This function receives input of whether a pokemon has been caught or not(Boolean). It will return
    a tuple of a random Pokemon's name in the 0th position (string), level in the 1st position(integer),
    and CP in the 2nd position (float)."""
    if catch:
        # randomly selects a pokemon from the pokemon list file
        pokemon = open('PokeList_v3.csv', 'r', )
        pokemon_reader = csv.reader(pokemon, delimiter=',')
        available_pokemon = list(pokemon_reader)
        available_pokemon.pop(0)
        poke_num = randint(0, 150)
        poke_name = available_pokemon[poke_num][1]
        level = randint(0, 30)
        cp = randint(int(available_pokemon[poke_num][2]), int(available_pokemon[poke_num][3]))

        return poke_name, level, cp


def math_problem_generator():
    """This function will output a random math equation to the user. If the user responds with the correct answer,
    a boolean value of True is returned as well with the output of a congratulatory message. If not, the user is
    notified that they failed and sent back to the main menu. In this case, a boolean value of False is returned."""
    # creates the random numbers to be used within the math equation
    num1 = randint(1, 10)
    num2 = randint(1, 10)
    symbol = randint(1, 3)
    # three different math equation structures are available to be used
    if symbol == 1:
        question = int(input(str(num1) + " + " + str(num2) + " = "))    # creates the math equation
        answer = num1 + num2    # calculates the answer to the math problem
        if question == answer:
            return True
        elif question != answer:
            print('You have failed!!!')
            return False

    elif symbol == 2:
        question = int(input(str(num1) + " - " + str(num2) + " = "))
        answer = num1 - num2
        if question == answer:
            return True
        elif question != answer:
            print('You have failed!!!')
            return False

    elif symbol == 3:
        question = int(input(str(num1) + " * " + str(num2) + " = "))
        answer = num1 * num2
        if question == answer:
            return True
        elif question != answer:
            print('You have failed!!!')
            return False


def pokemon_selector(account_name):
    """This function receives the argument of the account name to be used for the file name. It also will display all
    of the user's currently caught pokemon. The function returns the value (integer) of the pokemon they wish to select.
    """
    print('-' * 10 + ' Selector Menu ' + '-' * 10)
    # opens the user's file to access all of their pokemon
    pokemonFile = open('{}'.format(account_name), 'r')
    pokemon_reader = csv.reader(pokemonFile, delimiter=',')
    pokemon = list(pokemon_reader)

    # formats the way the pokemon will be displayed to the user
    for i in range(len(pokemon)):
        if i != (3 or 7 or 11):
            print('{}.{}    '.format(i + 1, pokemon[i][0]), end='')

        else:
            print('{}.{} '.format(i + 1, pokemon[i][0]))
            print()
    print('\n')
    # lets the user see the stats for an individual pokemon
    selection = int(input('Please enter the number of the pokemon you would like to view '
                          '(enter 0 to go back to the main menu):\n '))
    return selection


def display_pokemon_stats(num, account_name, candy_num):
    """This function recieves the parameters num(integer), account_name(string), and candy_num(integer) to be used to
    display all of the stats of a single pokemon to a user. It will call the level_up() and store_pokemon() functions if
     the user decides to level up their pokemon. It returns the  numerical value (integer) from if the user would like
     to level the selected pokemon up, or return to the main menu."""
    print('-' * 10 + ' Current Pokemon ' + '-' * 10)
    # opens the user's file to find the stats of the selected pokemon
    pokemonFile = open('{}'.format(account_name), 'r')
    pokemon_reader = csv.reader(pokemonFile, delimiter=',')
    pokemon = list(pokemon_reader)
    # formats the output of the pokemon's stats
    print('Name :          {}'.format(pokemon[num][0]))
    print('Combat Points:  {}'.format(pokemon[num][2]))
    print('Level:          {}'.format(pokemon[num][1]))
    print('Candies:        {}'.format(candy_num))
    choice = int(input('If you would like to level up this pokemon, please enter 1. Otherwise, enter 0:\n '))
    # levels up the pokemon by calling the level_up() and store_pokemon() functions
    if choice == 1:
        new_CP, new_level, candies = level_up(pokemon[num][1], pokemon[num][2], candy_num)
        store_pokemon(num, new_level, new_CP, account_name)
        return candies


def level_up(level, CP, candies):
    """This function receives the input of a pokemon's level(integer), CP(float), and the amount of candies the user
    has(integer). It will calculate the new stats of the leveled up pokemon and return the value of candies
    left(integer) and the pokemon's new level (integer) and CP level (float)."""
    level = int(level)
    CP = float(CP)
    if candies <= 0:
        print('You need more candies to level up. Try catching some pokemon!')
    # calculates the new level and CP if the pokemon is level 30 or less
    elif 1 <= level <= 30:
        candies -= 1
        level += 1
        CP = calculate_CP(level, CP)
        return CP, level, candies
    # calculates the new level and CP if the pokemon is between level 30 and level 40.
    elif 31 <= level < 40:
        candies -= 2
        level += 1
        CP = calculate_CP(level, CP)
        return CP, level, candies
    else:
        print('Your pokemon is at max level and cannot be leveled up!')


def calculate_CP(level, CP):
    """This function receives input of a pokemon's level(integer) and CP(float). It uses these values to
    calculate a new CP value and returns the new CP value (float)."""
    # calculates CP based on the level of the pokemon
    if 1 <= level <= 30:
        CP += CP * 0.0094 / (0.095 * math.sqrt(level))
        round(CP,2)
        return CP
    elif 31 <= level <= 40:
        CP += CP * 0.0045 / (0.095 * math.sqrt(level))
        round(CP,2)
        return CP


def store_pokemon(num, level, CP, fileID):
    """This function receives input of a pokemon's numerical position(integer), level(integer), and CP(float) and will
    update that pokemon's info with the new level and CP values."""
    # Reads in all the information of the user's file
    with open('{}'.format(fileID), 'r') as pokemonFile:
        pokemon_reader = csv.reader(pokemonFile, delimiter=',')
        pokemon = list(pokemon_reader)
        # updates the leveled up pokemon's data
        pokemon[num] = [pokemon[num][0], level, CP]

    # writes in the updated data to the user's file
    with open('{}'.format(fileID), 'w', newline='') as pokemonFile:
        pokemon_writer = csv.writer(pokemonFile, delimiter=',')
        for i in range(len(pokemon)):
            pokemon_writer.writerow(pokemon[i])


def battle(user1, pokemon1, user2, pokemon2):
    """"This function receives the input of a two usernames (string) and two pokemon numbers(integer), one from each
    user. The function will print the name of the user(string) and the pokemon(string) that won the battle."""
    # gets the pokemon information from the first user's file
    user_one = open('{}.csv'.format(user1), 'r')
    user_reader = csv.reader(user_one, delimiter=',')
    pokemon = list(user_reader)
    pokemon_one = pokemon[pokemon1 - 1]
    user_one.close()

    # gets the pokemon information from the second user's file
    user_two = open('{}.csv'.format(user2), 'r')
    user_reader = csv.reader(user_two, delimiter=',')
    pokemon = list(user_reader)
    pokemon_two = pokemon[pokemon2 - 1]
    user_two.close()

    # randomly chooses the winning pokemon. The pokemon with the higher level and combat points is more likely to win
    if pokemon_one[2] > pokemon_two[2]:
        number = randint(0, 30)
        if number > 10:
            print('After a long fought battle, {} and their {} reign supreme.'.format(user1, pokemon_one[0]))
        elif number <= 10:
            print('After a long fought battle, {} and their {} reign supreme.'.format(user2, pokemon_two[0]))

    elif pokemon_one[2] < pokemon_two[2]:
        number = randint(0, 30)
        if number > 10:
            print('After a long fought battle, {} and their {} reign supreme.'.format(user2, pokemon_two[0]))
        elif number <= 10:
            print('After a long fought battle, {} and their {} reign supreme.'.format(user1, pokemon_one[0]))

    elif pokemon_one[2] == pokemon_two[2]:
        number = randint(0, 20)
        if number > 10:
            print('After a long fought battle, {} and their {} reign supreme.'.format(user1, pokemon_one[0]))
        elif number <= 10:
            print('After a long fought battle, {} and their {} reign supreme.'.format(user2, pokemon_two[0]))


# has the user log into their account
username = input('Please enter your username (enter "none" if you don\'t have one): ')
fileID = account_login(username)

# begins the loop that starts the game
num = display_main_menu()
candies = 5.0
while num != 5:
    if num == 1:
        choice = pokemon_selector(fileID)
        if choice == 0:  # sends user back to the main menu
            pass
        else:   # shows all the stats of an individual pokemon in a sub menu
            choice -= 1
            candies = display_pokemon_stats(choice, fileID, candies)
    elif num == 2:
        # lets the user catch pokemon and updates their amount of rare candies if successful
        candy = catch_pokemon(candies)
        candies = candy
    elif num == 3:
        # user enters the necessary information to battle.
        user_one = input("Please enter the user name of the first challenger: ")
        poke_one = int(input('Enter the numerical position of the pokemon you would like to use in battle '
                             '(found in pokemon selector menu): '))
        user_two = input("Please enter the user name of the second challenger: ")
        poke_two = int(input('Enter the numerical position of the pokemon you would like to use in battle ('
                             'found in pokemon selector menu): '))
        print()
        # Battle function is called using the user provided information
        battle(user_one, poke_one, user_two, poke_two)

    elif num == 4:
        # lets the user switch to another account
        new_username = input('Enter the username of the account you would like to switch to: ')
        fileID = account_switch(new_username)
    # lets the user continue to make inputs within the menu until they quit the game
    num = display_main_menu()

print('Thanks for playing!')
