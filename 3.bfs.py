from collections import deque

class TreeNode:
    def _init_(self, value):
        self.value = value
        self.children = []

def bfs(node):
    if node is None:
        return
    queue = deque([node])  # Initialize the queue with the root
    while queue:
        current = queue.popleft()  # Dequeue the front element
        print(current.value, end=" ")  # Process the current node
        queue.extend(current.children)  # Enqueue all children

# Example Usage
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)

root.children = [child1, child2]
child1.children = [child3]

print("BFS:")
bfs(root)

"""
OUTPUT
-------------------
BFS:
1 2 3 4 
-------------------
"""
