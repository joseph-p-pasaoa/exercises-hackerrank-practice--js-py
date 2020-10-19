# Preorder Traversal

def preOrder(root):
    def recursiveTraversal(node):
        if not node:
            return

        values.append(node.info)
        recursiveTraversal(node.left)
        recursiveTraversal(node.right)

    values = []
    recursiveTraversal(root)

    output = ' '.join(map(str, values))
    print(output)

# Passed 6 test cases successfully.
