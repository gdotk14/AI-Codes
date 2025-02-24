# Table-Driven Cleaning Agent for Rooms A, B, C, D
rooms = {'A': 'Dirty', 'B': 'Dirty', 'C': 'Clean', 'D': 'Dirty'}  # Initial state of rooms
current_room = 'A'  # Start at Room A
actions_table = {
    ('A', 'Dirty'): 'Clean',
    ('A', 'Clean'): 'MoveToNext',
    ('B', 'Dirty'): 'Clean',
    ('B', 'Clean'): 'MoveToNext',
    ('C', 'Dirty'): 'Clean',
    ('C', 'Clean'): 'MoveToNext',
    ('D', 'Dirty'): 'Clean',
    ('D', 'Clean'): 'MoveToNext'
}

# Function to determine the next room in sequence
def get_next_room(current):
    order = ['A', 'B', 'C', 'D']
    return order[(order.index(current) + 1) % 4]

# Agent Execution
while True:
    print(f"Current Room: {current_room}, State: {rooms[current_room]}")
    action = actions_table[(current_room, rooms[current_room])]
    
    if action == 'Clean':
        rooms[current_room] = 'Clean'
        print(f"Action: {action} → {current_room} is now clean.")
    elif action == 'MoveToNext':
        print(f"Action: {action} → Moving to the next room.")
        current_room = get_next_room(current_room)
    
    # Check if all rooms are clean
    if all(state == 'Clean' for state in rooms.values()):
        print("All rooms are clean. Task completed!")
        break

"""
OUTPUT
-------------------------
Current Room: A, State: Dirty
Action: Clean → A is now clean.
Current Room: A, State: Clean
Action: MoveToNext → Moving to the next room.
Current Room: B, State: Dirty
Action: Clean → B is now clean.
Current Room: B, State: Clean
Action: MoveToNext → Moving to the next room.
Current Room: C, State: Clean
Action: MoveToNext → Moving to the next room.
Current Room: D, State: Dirty
Action: Clean → D is now clean.
All rooms are clean. Task completed!
-------------------------
"""
