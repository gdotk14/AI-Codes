class TreeNode:
    def _init_(self, value):
        self.value = value
        self.children = []

def dfs_recursive(node):
    if node is None:
        return
    print(node.value, end=" ")  # Process the current node
    for child in node.children:
        dfs_recursive(child)

# Example Usage
root = TreeNode(1)
child1 = TreeNode(2)
child2 = TreeNode(3)
child3 = TreeNode(4)

root.children = [child1, child2]
child1.children = [child3]

print("DFS:")
dfs_recursive(root)

"""
OUTPUT
--------------------
DFS:
1 2 4 3
--------------------
"""
