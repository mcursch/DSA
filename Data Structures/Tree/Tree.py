import collections

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def print_dfs(self):
        if self.left:
            self.left.printTree()
        print( self. data )
        if self.right:
            self.right.printTree()

    def print_bfs(self):
        result = []
        q = collections.deque([root])

        while q:
            node = q.popleft()
            result.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return result

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(7)
root.insert(13)
root.insert(20)
print(root.print_bfs())


