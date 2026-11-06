# Mystery Island: The Lost Lighthouse

## About the Game

Mystery Island: The Lost Lighthouse is a Python-based text adventure game. The player explores a mysterious island, collects useful items, makes decisions, manages energy, and tries to reach the lighthouse to escape.

## Game Features

- Five locations: Beach, Jungle, Cave, Old Bridge, and Lighthouse.
- Starting energy of 5 points.
- Collectible items: Rope and Lantern.
- Three meaningful decisions with different consequences.
- Movement restrictions based on collected items.
- Energy management system.
- Winning and losing conditions.
- Quit and replay functionality.
- Input validation to handle invalid commands.

## Requirements

- Python 3 installed on your computer.
- No external Python libraries are required.

## How to Run the Game

1. Open your terminal.
2. Navigate to the project folder.
3. Run the following command:

```bash
python3 main.py
```

## Game Rules

1. The player starts at the Beach with 5 energy points.
2. The player must explore the island and collect useful items.
3. The Rope is collected in the Jungle and is required to cross the Old Bridge.
4. The Lantern is collected in the Cave and is required to enter the Lighthouse.
5. Players encounter three decisions in the Jungle, Cave, and Old Bridge.
6. Dangerous choices consume additional energy.
7. Moving between locations also consumes energy.
8. The player loses when their energy reaches zero.
9. The player wins by reaching the Lighthouse with the Lantern while having energy remaining.
10. The player can quit or start a new adventure after a game ends.

## How to Run the Tests

To run the automated tests, open your terminal in the project folder and enter:

```bash
python3 -m unittest discover -s tests -v
```

The project currently contains 16 automated tests covering game logic, movement, item collection, energy management, and winning and losing conditions.

## Project Structure

```text
mystery_island/
├── main.py
├── game.py
├── README.md
└── tests/
    └── test_game.py
```

## Technologies Used

- Python 3
- Python unittest module

## Known Limitations

- The game uses a text-based interface rather than graphics.
- The game supports one player at a time.
- Game progress is not saved after the program closes.
- The player must complete the adventure within the available energy.

## Author

Mystery Island: The Lost Lighthouse was developed as a beginner Python programming project.