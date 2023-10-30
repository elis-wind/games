"""
Goose Game Simulation
This script simulates a simple board game with dice rolls and player movement.

This software is released under the MIT License.
For the full license text, please see the LICENSE file.
"""

import random


class Player:
	#Represents a player in the Goose Game
    def __init__(self, name):
        self.name = name
        self.position = 0

    def __str__(self):
        return self.name

    def move(self, step1, step2):
        self.position += step1 + step2


players = set()


def add_players():
	#Add players to the game
    while True:
        player_name = input("Add player: ")
        try:

            #Check for an empty player name
            if not player_name.strip():
                raise ValueError("Player name cannot be empty")
            
            #Check if player name is a string
            if not player_name.isalpha():
                raise ValueError("Player name must contain only alphabetic characters")
            
            #Check the number of players
            if player_name.lower() == "start":
                if len(players) < 2:
                    print("You need at least two players to start the game.")
                else:
                    print("\nStarting the game with {} players.".format(len(players)))
                    break # Exit the loop to start the game
            
            #Prevent duplicates in players
            elif any(player.name == player_name for player in players):
                print("{}: already existing player".format(player_name))
            
            #Return players list
            else:
                player = Player(player_name)
                players.add(player)
                print("Players: {}".format(", ".join(str(player) for player in players)))
        
        except ValueError as e:
            print("Error:", e)

def roll_dice():
	#Roll the dice
    return random.randint(1, 6)


def main():
	#Welcome message
    print('''
    Welcome to the GOOSE GAME!
    Enter players' names and write "start" to begin the game
    Press Enter to roll the dice.
    ''')

    add_players()
    goose = [5, 9, 14, 18, 23, 27]

    while True:
    	#Rolling the dice
        for player in players:
            input(f'{player} rolls: ')
            step1, step2 = roll_dice(), roll_dice()
            initial_position = player.position
            player.move(step1, step2)
            
            #Bridge condition
            if player.position == 6:
                print("{} rolls {}, {}. {} moves from {} to The Bridge. {} jumps to 12".format(
                    player,step1,step2,player,initial_position,player))
                player.position = 12

            #Goose condition
            elif player.position in goose:
                new_position = player.position + step1 + step2

                #Double Goose checking
                if new_position in goose:
                    new_position2 = new_position + step1 + step2
                    print("{} rolls {}, {}. {} moves from {} to {}. The Goose! {} moves again and goes to {}. The Goose! {} moves again and goes to {}".format(
                        player,step1,step2,player,initial_position,player.position,player,new_position,player,new_position2))
                    player.position = new_position2
                else:
                    print("{} rolls {}, {}. {} moves from {} to {}. The Goose! {} moves again and goes to {}".format(
                        player,step1,step2,player,initial_position,player.position,player,new_position))
                    player.position = new_position
            
            #Game condition
            elif player.position < 63:
                print("{} rolls {}, {}. {} moves from {} to {}".format(
                    player,step1,step2,player,initial_position,player.position))
            
            #Bounce condition
            elif player.position > 63:
                bounce = player.position - 63
                new_position = 63 - bounce
                print("{} rolls {}, {}. {} moves from {} to 63. {} bounces! {} returns to {}".format(
                    player,step1,step2,player,initial_position,player,player,new_position))
                player.position = new_position
            
            #Victory condition
            elif player.position == 63:
                print("{} rolls {}, {}. {} moves from {} to {}. {} Wins!".format(
                    player,step1,step2,player,initial_position,player.position,player))
                break
        else:
            continue
        break


if __name__ == "__main__":
    main()
