# Goose Game Simulation

## Overview

The Goose Game Simulation is a Python script that simulates a simple board game with dice rolls and player movement.

## Getting Started

To use the Goose Game Simulation, follow these steps:

1. Clone the Repository:

    Clone this repository to your local machine using git clone.

2. Run the Game:

    Execute the script by running the `goose_game.py` file in a Python environment.

3. Add Players:

    You can add as much players as you want by entering their names when prompted. To start the game, simply enter `start` when you're ready to begin.


4. Roll the Dice:

    Players take turns rolling the dice by pressing Enter, and their positions are updated based on the game rules.

5. Game Rules

    - **Players**: The game requires a minimum of two players to begin.

    - **Movement**: Players take turns rolling two six-sided dice and move forward a number of steps equal to the sum of the dice.

    - **Special Conditions**:

        *The Bridge*: When a player lands on position 6, they immediately jump to position 12.

        *The Goose*: When a player lands on positions 5, 9, 14, 18, 23, or 27, they move forward twice. If they land again on one of these Goose positions, they move forward once more.

    - **Winning**: The game continues until a player lands exactly on position 63, at which point they are declared the winner.

    - **Overshooting**: If a player's move takes them beyond position 63, they bounce back to the number of steps that overshoot 63.

## Python Version Compatibility

This software is compatible with Python version 3.7.

## License

This software is released under the MIT License. For details, please see the `LICENSE` file.
