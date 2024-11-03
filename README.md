## About the Author
This project was developed by [Mkdad Taleb], a [University class : 6] student at [Damascus University].

# Logic Magnets Game

Logic Magnets Game is a puzzle game where you move magnets to reach the goal. The game uses advanced search algorithms like DFS and BFS to find optimal solutions.

## Table of Contents

Logic_Magnets_Game/
│   ├── Actions/            # Directory for action-related modules
│   │   ├── magnets.py      # Module for magnet actions
│   │   ├── moveBlocks.py   # Module for moving blocks
│   │   ├── pull.py         # Module for pulling actions
│   │   ├── push.py         # Module for pushing actions
│   ├── Structures/         # Directory for structural components
│   │   ├── level.py        # Module defining game levels
│   │   ├── state.py        # Module defining game states
│   │   └── magnets.py      # Module defining magnets
│   ├── Logic/              # Directory for logic-related modules
│   │   ├── bfs.py          # Module for BFS algorithm
│   │   ├── dfs.py          # Module for DFS algorithm
│   │   ├── gameplay.py     # Module for gameplay logic
│   │   ├── explore_search_space.py # Module for exploring search space
│   ├── main.py             # Main entry point of the game
│   └── utils.py            # Utility functions and helpers
├── README.md               # This file, explaining the project
└── requirements.txt        # List of dependencies


## Description
Logic Magnets Game is an engaging puzzle game where you strategically move magnets on a grid to achieve the goal state. The game employs intelligent search algorithms such as DFS and BFS to determine the best moves.

## Installation
To install the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/mkdad-123/logic-magnets-game.git

2. Navigate to the project directory:
    cd Logic-Magnets-Game
3. Install the dependencies:
    pip install -r requirements.txt

## Contribution
We welcome contributions! If you would like to contribute, please follow these steps:

1. **Fork the repository**.
2. **Create a new branch**.
    ```bash
    git checkout -b feature/your-feature-name
    ```
3. **Make your changes**.
4. **Commit your changes**.
    ```bash
    git commit -m "Add feature: your feature name"
    ```
5. **Push to the branch**.
    ```bash
    git push origin feature/your-feature-name
    ```
6. **Open a Pull Request**.


## Dependencies
The project uses the following libraries and dependencies:

- `numpy`
- `collections`
- `copy`

## usage 
To run the game, use the following command:
    python Game/main.py
