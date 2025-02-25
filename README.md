# LIST OF AI PROBLEMS & SOLUTIONS 
## GAURAV KUMAR-VU22CSEN0101555
## ARTIFICIAL INTELLIGENCE LAB-CSEN2031P

---

## 1. VACUUM CLEANER PROBLEM  
**Problem Statement:**  
A vacuum cleaner operates in a 2-room environment where each room can be **clean** or **dirty**. The vacuum must autonomously decide where to move and when to clean, minimizing its total actions.  

**Conditions:**  
- The environment consists of **two rooms (A & B)**.  
- The vacuum cleaner can be in **one of the rooms** at any time.  
- It can perform the actions: **Move Left, Move Right, Clean**.  
- The goal is to clean all dirty rooms efficiently.  

**Solution Approach:**  
- **Simple Reflex Agent:** The vacuum follows a predefined rule (if the current room is dirty, clean it; otherwise, move to the next room).  
- **Table-Driven Approach:** Uses a lookup table to determine actions based on the history of previous states.  

---

## 2. WATER JUG PROBLEM  
**Problem Statement:**  
Given two jugs with different capacities (e.g., 4L and 3L), measure an exact amount of water (e.g., 2L) using a sequence of valid operations.  

**Conditions:**  
- You can **fill, empty, or transfer** water between jugs.  
- The goal is to reach a specific quantity using the least number of steps.  

**Solution Approach:**  
- Uses **State-Space Search (BFS or DFS)** to explore all possible states of water distribution.  
- **Graph representation** where each node represents a state (amount of water in both jugs).  

---

## 3.a. BREADTH-FIRST SEARCH (BFS)  
**Problem Statement:**  
BFS is a **graph traversal algorithm** used to explore nodes layer by layer, ensuring the shortest path in an **unweighted graph**.  

**Conditions:**  
- It starts from a **source node** and explores all its adjacent nodes before moving to the next level.  
- It guarantees finding the shortest path in an **unweighted graph**.  

**Solution Approach:**  
- Uses a **queue (FIFO)** to keep track of nodes to be explored.  
- Commonly used in **shortest path problems, AI search strategies, and network exploration**.  

---

## 3.b. DEPTH-FIRST SEARCH (DFS)  
**Problem Statement:**  
DFS is a **graph traversal algorithm** that explores as far as possible along one branch before backtracking.  

**Conditions:**  
- It starts from a **source node** and moves deeper into the graph before returning to unexplored branches.  
- Suitable for **solving maze problems, cycle detection, and topological sorting**.  

**Solution Approach:**  
- Uses a **stack (either explicit or via recursion)** to explore nodes.  
- Works efficiently for **searching and traversing large graphs**.  

---

## 4. MONKEY AND BANANA PROBLEM  
**Problem Statement:**  
A monkey is in a room where bananas are hanging from the ceiling. The monkey must figure out how to reach them using a set of available actions.  

**Conditions:**  
- The monkey can **walk, climb, push a box, or grab** the bananas.  
- It must decide the best sequence of actions to retrieve the bananas.  

**Solution Approach:**  
- Represented as a **state-space search problem**.  
- Uses **AI search algorithms (DFS, BFS, A*)** to determine the shortest sequence of actions.  

---

## 5. EIGHT PUZZLE PROBLEM  
**Problem Statement:**  
The **8-puzzle game** consists of a 3x3 grid with numbered tiles (1-8) and one empty space. The goal is to move tiles into a specified goal state using the minimum number of moves.  

**Conditions:**  
- Tiles can move **up, down, left, or right** into the empty space.  
- The goal state is a predefined arrangement of numbers.  

**Solution Approach:**  
- Uses **heuristic search algorithms** like **A* Algorithm (Manhattan Distance heuristic)** to minimize moves.  
- **Branch and Bound or BFS** can also be used for an optimal solution.  

---

## 6. HANGMAN GAME  
**Problem Statement:**  
A word-guessing game where the player has a limited number of attempts to guess the correct word before the "hangman" is fully drawn.  

**Conditions:**  
- The player can guess **one letter at a time**.  
- Incorrect guesses reduce remaining attempts.  
- The game ends when the player either **guesses the full word** or **runs out of attempts**.  

**Solution Approach:**  
- Implements **string manipulation and condition checking**.  
- Uses Python **loops and conditional statements** to verify correct/incorrect guesses.  

---

## 7. EIGHT QUEENS PROBLEM  
**Problem Statement:**  
The goal is to place **eight queens** on an 8×8 chessboard so that no two queens attack each other (i.e., no two queens share the same row, column, or diagonal).  

**Conditions:**  
- Each queen must be placed **in a different row and column**.  
- No two queens can be **on the same diagonal**.  

**Solution Approach:**  
- Uses **Backtracking Algorithm** to explore possible board configurations.  
- Can also be solved using **Genetic Algorithms or Constraint Satisfaction Problems (CSP)**.  

---

