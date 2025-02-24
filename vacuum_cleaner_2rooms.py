def vacuum_world():
    goal_state = {'A': '0', 'B': '0'}

    location_input = input("Enter Location of Vacuum:") 
    status_input = input("Enter status of " + location_input+":")
    status_input_complement = input("Enter status of other room:")

    if location_input == 'A':
        print("Vacuum is placed in Location A")
        if status_input == '1':
            print("Location A is Dirty.")
            goal_state['A'] = '0'
            print("Location A has been Cleaned.")

            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("Moving right to the Location B. ")
                goal_state['B'] = '0'
                print("Location B has been Cleaned. ")
            else:
                print("No action")
                print("Location B is already clean.")

        if status_input == '0':
            print("Location A is already clean ")
            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("Moving RIGHT to the Location B. ")
                goal_state['B'] = '0'
                print("Location B has been Cleaned. ")
            else:
                print("No action ")
                print("Location B is already clean.")

    else:
        print("Vacuum is placed in location B")
        if status_input == '1':
            print("Location B is Dirty.")
            goal_state['B'] = '0'
            print("Location B has been Cleaned.")

            if status_input_complement == '1':
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                goal_state['A'] = '0'
                print("Location A has been Cleaned.")

        else:
            print("Location B is already clean.")

            if status_input_complement == '1':  
                print("Location A is Dirty.")
                print("Moving LEFT to the Location A. ")
                goal_state['A'] = '0'
                print("Location A has been Cleaned. ")
            else:
                print("No action ")
                print("Location A is already clean.")

    print("GOAL STATE achieved: ")
    print(goal_state)


vacuum_world()

"""
OUTPUT
-----------------------------
Enter Location of Vacuum:A
Enter status of A:1
Enter status of other room:0
Vacuum is placed in Location A
Location A is Dirty.
Location A has been Cleaned.
No action
Location B is already clean.
GOAL STATE achieved: 
{'A': '0', 'B': '0'}
----------------------------
"""
