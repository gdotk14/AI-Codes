# Simple Reflex Agent for Cleaning Rooms
# Define initial states: all rooms are dirty
rooms = {'A': 'Dirty', 'B': 'Dirty', 'C': 'Dirty', 'D': 'Dirty'}
current_room = 'A'  # Agent starts at Room A

# Function to move to the next room in order
def get_next_room(current):
    order = ['A', 'B', 'C', 'D']
    return order[(order.index(current) + 1) % 4]  # Cycle through rooms A → B → C → D → A

# Function for the Simple Reflex Agent
def simple_reflex_agent():
    global current_room  # Keep track of the current room
    print("Initial State:", rooms)
    
    while True:
        print(f"\nAgent is in Room {current_room}")
        
        if rooms[current_room] == 'Dirty':
            print(f"Room {current_room} is Dirty → Cleaning...")
            rooms[current_room] = 'Clean'  # Update room state to Clean
            print(f"Room {current_room} is now Clean.")
        else:
            print(f"Room {current_room} is already Clean → Moving to the next room.")
        
        # Check if all rooms are clean
        if all(state == 'Clean' for state in rooms.values()):
            print("\nAll rooms are clean! Cleaning process complete.")
            break
        
        # Move to the next room
        current_room = get_next_room(current_room)

# Execute the agent
simple_reflex_agent()

"""
OUTPUT
-------------------
Initial State: {'A': 'Dirty', 'B': 'Dirty', 'C': 'Dirty', 'D': 'Dirty'}

Agent is in Room A
Room A is Dirty → Cleaning...
Room A is now Clean.

Agent is in Room B
Room B is Dirty → Cleaning...
Room B is now Clean.

Agent is in Room C
Room C is Dirty → Cleaning...
Room C is now Clean.

Agent is in Room D
Room D is Dirty → Cleaning...
Room D is now Clean.

All rooms are clean! Cleaning process complete.
-------------------
"""
