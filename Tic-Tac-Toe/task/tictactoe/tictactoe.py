# Tic-Tac-Toe
# Author: Jason Tolbert (https://github.com/jasonalantolbert)
# Python Version: 3.6


# import re module
import re

# possible victory patterns for X and O written as regular expressions
x_solution_list = [
    r"XXX\w\w\w\w\w\w", r"\w\w\wXXX\w\w\w", r"\w\w\w\w\w\wXXX", r"X\w\wX\w\wX\w\w", r"\wX\w\wX\w\wX\w",
    r"\w\wX\w\wX\w\wX", r"X\w\w\wX\w\w\wX", r"\w\wX\wX\wX\w\w"]

o_solution_list = [
    r"OOO\w\w\w\w\w\w", r"\w\w\wOOO\w\w\w", r"\w\w\w\w\w\wOOO", r"O\w\wO\w\wO\w\w", r"\wO\w\wO\w\wO\w",
    r"\w\wO\w\wO\w\wO", r"O\w\w\wO\w\w\wO", r"\w\wO\wO\wO\w\w"]

# creates board layout and converts it to a list, which is
# then used to to form a matrix that will be used for coordinates
tic_tac_input = "_________"
tic_tac_list = list(tic_tac_input)
tic_tac_matrix = [tic_tac_list[6:9], tic_tac_list[3:6], tic_tac_list[0:3]]

move_counter = 1
# this while loop encompasses the rest of the program
# and will run perpetually until either a player wins
# or there is a draw; in either case, the program will
# output the game result and terminate

while True:
    # prints tic-tac-toe board

    def print_board():
        print(f'''
    {1} {2} {3}
  ---------
{3} | {tic_tac_list[0]} {tic_tac_list[1]} {tic_tac_list[2]} |
{2} | {tic_tac_list[3]} {tic_tac_list[4]} {tic_tac_list[5]} |
{1} | {tic_tac_list[6]} {tic_tac_list[7]} {tic_tac_list[8]} |
  ---------
                    ''')
    if move_counter == 1:
        print_board()

    # determines whether X or O is playing
    if not move_counter % 2 == 0:
        current_player = "X"
    else:
        current_player = "O"

    # this if-while statement checks for valid coordinate input

    valid_coords = False

    while not valid_coords:
        coords = input("Enter coords: ")
        if re.match("\D", list(coords)[2]) or re.match("\D", list(coords)[0]):
            print("You should enter numbers!")
        elif not 1 <= int(list(coords)[2]) <= 3 or not 1 <= int(list(coords)[0]) <= 3:
            print("Coordinates should be from 1 to 3!")
        elif re.match("[XO]", tic_tac_matrix[int(list(coords)[2]) - 1][int(list(coords)[0]) - 1]):
            print("This cell is occupied! Choose another one!")
        else:
            valid_coords = True

    # assigns each coord to the row and column variables
    row, column = coords.split()

    # inserts X into matrix, clears board, and repopulates board with new matrix values
    tic_tac_matrix[int(column) - 1][int(row) - 1] = current_player
    tic_tac_matrix = tic_tac_matrix[::-1]
    tic_tac_list.clear()
    tic_tac_input = ""
    for column in tic_tac_matrix:
        for row in column:
            tic_tac_list.append(row)
    for item in tic_tac_list:
        tic_tac_input += item
    tic_tac_matrix = tic_tac_matrix[::-1]
    move_counter += 1

    print_board()

    # from here on out, the program checks the board to determine the result of the game

    # x_wins: is true if X gets three in a row, false otherwise
    # o_wins: is true if O gets three in a row, false otherwise
    # complete_board: is true if no blank spaces (underscores) are present in the board
    # check_types: list of checks for the program to run
    if move_counter > 5:

        check_types = ["X Wins", "O Wins", "Complete Board"]

        x_wins = False
        o_wins = False
        complete_board = True
        end_check = False

        while (not x_wins and not o_wins) and complete_board:

            for check_type in check_types:

                index_to_check = 0

                if check_type == "X Wins":

                    # cycles through x_solution_list; if any solutions
                    # match the board, x_wins is set to true
                    while index_to_check < len(x_solution_list):
                        if re.match(x_solution_list[index_to_check], tic_tac_input):
                            x_wins = True
                            break
                        index_to_check += 1

                if check_type == "O Wins":

                    # cycles through o_solution_list; if any solutions
                    # match the board, o_wins is set to true
                    while index_to_check < len(o_solution_list):
                        if re.match(o_solution_list[index_to_check], tic_tac_input):
                            o_wins = True
                            break
                        index_to_check += 1

                if check_type == "Complete Board":

                    # checks the board for blank spaces (underscores)
                    while index_to_check < len(tic_tac_list):
                        if tic_tac_list[index_to_check] == "_":
                            complete_board = False
                            break
                        index_to_check += 1
                    if complete_board:
                        break
            if complete_board:
                break

        # below are the result returners. these parts of the program
        # are responsible for returning the game result:
        # "Game not finished", "Draw", "X wins", or "Impossible".
        # once a result is returned, the program will exit.

        # returns Draw result if neither X nor O won.
        # further returners cannot execute if this one does.
        if not x_wins and not o_wins and complete_board:
            print("Draw")
            input("Press Enter to exit.")
            exit()

        # returns X wins result if X wins.
        # further returners cannot execute if this one does.
        if x_wins:
            print("X wins")
            input("Press Enter to exit.")
            exit()

        # returns O wins result if O wins.
        # note: the if condition here is redundant; if the program makes it this far
        # then none of the other returners executed, so by process of elimination
        # O must have won, and we can simply print "O wins" without the need for any
        # conditional statements. it is included regardless for the sake of
        # making the code easier to understand.
        if o_wins:
            print("O wins")
            input("Press Enter to exit.")
            exit()
