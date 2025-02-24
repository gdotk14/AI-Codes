class MonkeyBananaProblem:
    def __init__(self):
        self.room = [["Empty" for _ in range(3)] for _ in range(3)]
        self.monkey1_pos = (0, 0)
        self.monkey2_pos = (0, 1)
        self.banana_pos = (1, 2)
        self.chair_pos = (2, 2)
        self.chair_picked = False

    def display_room(self):
        print("Room Layout:")
        for i in range(3):
            row = []
            for j in range(3):
                if (i, j) == self.monkey1_pos:
                    row.append("Monkey1")
                elif (i, j) == self.monkey2_pos:
                    row.append("Monkey2")
                elif (i, j) == self.banana_pos:
                    row.append("Banana")
                elif (i, j) == self.chair_pos and not self.chair_picked:
                    row.append("Chair")
                else:
                    row.append("Empty")
            print(row)
        print()

    def move_monkey(self, monkey, target_pos):
        if monkey == 1:
            self.monkey1_pos = target_pos
        elif monkey == 2:
            self.monkey2_pos = target_pos
        self.display_room()

    def find_path(self, start, end):
        x1, y1 = start
        x2, y2 = end
        moves = []
        while x1 != x2:
            x1 += 1 if x1 < x2 else -1
            moves.append((x1, y1))
        while y1 != y2:
            y1 += 1 if y1 < y2 else -1
            moves.append((x1, y1))
        return moves

    def pick_chair(self, monkey):
        if monkey == 1 and self.monkey1_pos == self.chair_pos:
            self.chair_picked = True
        elif monkey == 2 and self.monkey2_pos == self.chair_pos:
            self.chair_picked = True

    def run(self):
        self.display_room()
        # Calculate paths
        monkey1_to_chair = self.find_path(self.monkey1_pos, self.chair_pos)
        monkey2_to_chair = self.find_path(self.monkey2_pos, self.chair_pos)
        chair_to_banana = self.find_path(self.chair_pos, self.banana_pos)

        monkey1_path = monkey1_to_chair + chair_to_banana
        monkey2_path = monkey2_to_chair + chair_to_banana

        # Simulation
        for step in range(max(len(monkey1_path), len(monkey2_path))):
            if step < len(monkey1_path):
                self.move_monkey(1, monkey1_path[step])
                if self.monkey1_pos == self.chair_pos and not self.chair_picked:
                    self.pick_chair(1)
                    print("Monkey1 picks up the chair.")
                if self.monkey1_pos == self.banana_pos and self.chair_picked:
                    print("Monkey1 climbs the chair and grabs the banana! Monkey1 wins!")
                    return

            if step < len(monkey2_path):
                self.move_monkey(2, monkey2_path[step])
                if self.monkey2_pos == self.chair_pos and not self.chair_picked:
                    self.pick_chair(2)
                    print("Monkey2 picks up the chair.")
                if self.monkey2_pos == self.banana_pos and self.chair_picked:
                    print("Monkey2 climbs the chair and grabs the banana! Monkey2 wins!")
                    return


# Run the game
problem = MonkeyBananaProblem()
problem.run()

"""
OUTPUT
---------------------
Room Layout:
['Monkey1', 'Monkey2', 'Empty']
['Empty', 'Empty', 'Banana']
['Empty', 'Empty', 'Chair']

Room Layout:
['Empty', 'Monkey2', 'Empty']
['Monkey1', 'Empty', 'Banana']
['Empty', 'Empty', 'Chair']

Room Layout:
['Empty', 'Empty', 'Empty']
['Monkey1', 'Monkey2', 'Banana']
['Empty', 'Empty', 'Chair']

Room Layout:
['Empty', 'Empty', 'Empty']
['Empty', 'Monkey2', 'Banana']
['Monkey1', 'Empty', 'Chair']

Room Layout:
['Empty', 'Empty', 'Empty']
['Empty', 'Empty', 'Banana']
['Monkey1', 'Monkey2', 'Chair']

Room Layout:
['Empty', 'Empty', 'Empty']
['Empty', 'Empty', 'Banana']
['Empty', 'Monkey1', 'Chair']

Room Layout:
['Empty', 'Empty', 'Empty']
['Empty', 'Empty', 'Banana']
['Empty', 'Monkey1', 'Monkey2']

Monkey2 picks up the chair.
Room Layout:
['Empty', 'Empty', 'Empty']
['Empty', 'Empty', 'Banana']
['Empty', 'Empty', 'Monkey1']

Room Layout:
['Empty', 'Empty', 'Empty']
['Empty', 'Empty', 'Monkey2']
['Empty', 'Empty', 'Monkey1']

Monkey2 climbs the chair and grabs the banana! Monkey2 wins!
---------------------
"""
