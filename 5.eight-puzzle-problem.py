class Puzzle8:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state

    def is_goal(self, state):
        return state == self.goal_state

    def get_neighbors(self, state):
        neighbors = []
        zero_index = state.index(0)  # Find the blank space (0)
        row, col = divmod(zero_index, 3)  # Convert to row and column

        # Define possible moves: (row_offset, col_offset)
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for move in moves:
            new_row, new_col = row + move[0], col + move[1]
            if 0 <= new_row < 3 and 0 <= new_col < 3:  # Valid move
                new_index = new_row * 3 + new_col
                new_state = list(state)
                # Swap the blank space with the adjacent tile
                new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
                neighbors.append(tuple(new_state))

        return neighbors

    def solve(self):
        stack = [(self.start_state, [])]  # (state, path)
        visited = set()

        while stack:
            current_state, path = stack.pop()  # Get the last added state (DFS)

            if self.is_goal(current_state):
                return path  # Return the path to the goal

            if current_state in visited:
                continue
            visited.add(current_state)

            for neighbor in self.get_neighbors(current_state):
                if neighbor not in visited:
                    new_path = path + [neighbor]
                    stack.append((neighbor, new_path))

        return None  # No solution found

if __name__ == "__main__":
    # Initial state (0 represents the blank space)
    start = (1, 2, 3, 0, 5, 6, 4, 7, 8)
    # Goal state
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    puzzle = Puzzle8(start, goal)
    solution = puzzle.solve()

    if solution:
        print("Solution found!")
        for step in solution:
            print(step)
    else:
        print("No solution found.")

"""
OUTPUT
--------------------------
Solution found!
(1, 2, 3, 5, 0, 6, 4, 7, 8)
(1, 2, 3, 5, 6, 0, 4, 7, 8)
(1, 2, 3, 5, 6, 8, 4, 7, 0)
(1, 2, 3, 5, 6, 8, 4, 0, 7)
(1, 2, 3, 5, 6, 8, 0, 4, 7)
(1, 2, 3, 0, 6, 8, 5, 4, 7)
(1, 2, 3, 6, 0, 8, 5, 4, 7)
(1, 2, 3, 6, 8, 0, 5, 4, 7)
(1, 2, 3, 6, 8, 7, 5, 4, 0)
(1, 2, 3, 6, 8, 7, 5, 0, 4)
(1, 2, 3, 6, 8, 7, 0, 5, 4)
(1, 2, 3, 0, 8, 7, 6, 5, 4)
(1, 2, 3, 8, 0, 7, 6, 5, 4)
(1, 2, 3, 8, 7, 0, 6, 5, 4)
(1, 2, 3, 8, 7, 4, 6, 5, 0)
(1, 2, 3, 8, 7, 4, 6, 0, 5)
(1, 2, 3, 8, 7, 4, 0, 6, 5)
(1, 2, 3, 0, 7, 4, 8, 6, 5)
(1, 2, 3, 7, 0, 4, 8, 6, 5)
(1, 2, 3, 7, 4, 0, 8, 6, 5)
(1, 2, 3, 7, 4, 5, 8, 6, 0)
(1, 2, 3, 7, 4, 5, 8, 0, 6)
(1, 2, 3, 7, 4, 5, 0, 8, 6)
(1, 2, 3, 0, 4, 5, 7, 8, 6)
(1, 2, 3, 4, 0, 5, 7, 8, 6)
(1, 2, 3, 4, 5, 0, 7, 8, 6)
(1, 2, 3, 4, 5, 6, 7, 8, 0)
--------------------------
"""
