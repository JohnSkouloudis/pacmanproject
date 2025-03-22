# Berkeley Pacman Project for AI 🍒👻

Welcome to the Berkeley Pacman Project repository! This project is a fun and interactive way to learn about artificial intelligence through the classic game of Pacman. Whether you're diving into search algorithms, multi-agent systems, or reinforcement learning, this project has something for you.

## Overview 🎮

The Berkeley Pacman Project is widely used in AI courses to introduce various fundamental AI concepts. In this project, you'll explore:
- **Search Algorithms**: Learn to navigate Pacman through mazes using algorithms like DFS, BFS, and A*.
- **Adversarial Search**: Develop strategies for multi-agent environments, where ghosts are your adversaries.
- **Reinforcement Learning**: Experiment with techniques that allow Pacman to learn from experience.
- **Multi-Agent Systems**: Understand how multiple agents interact in a competitive environment.

## Repository Structure 🗂️

Here's an overview of the key files and directories included in this repository:

- **`pacman.py`**  
  The main driver file to start the Pacman game. Run this file to launch the game and experiment with different agents.

- **`search.py`**  
  Contains implementations of various search algorithms used to navigate Pacman through the maze.

- **`multiAgents.py`**  
  Implements multi-agent search techniques, including strategies for both Pacman and the ghosts.
  
- **`README.md`**  
  This file! It provides an overview of the project, installation instructions, and usage details.

- **`agents/`**  
  A directory (if present) that might contain custom agent implementations or additional project resources.

## Installation & Setup 🛠️

1. **Clone the Repository**:  
   Open your terminal and run:
   ```bash
   git clone https://github.com/JohnSkouloudis/pacmanproject.git

2. **Navigate to the Project Directory**:
   ```bash
    cd pacmanproject

## Running the Project 🚀

- **To start the Pacman game, run the following command in your terminal**:
  ```bash
    python pacman.py

- **You can also experiment with different agents by specifying command-line arguments. For example, to run a search-based agent**:
  ```bash
    python pacman.py -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
