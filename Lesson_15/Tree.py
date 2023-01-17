class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val)
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val)
            return self.right.findval(find_val)
        else:
            print(str(self.id_node) + ' is found')

    def add_elements(self, list_of_node):
        for node in list_of_node:
            if node is None:
                continue
            self.insert(node)


    def min(self):
        if self.left is None:
            print(self.id_node)
        else:
            print(self.left.min())

    def max(self):
        if self.right is None:
            print(self.id_node)
        else:
            print(self.right.max())

    def delete(self, node):
        if not self.findval(node):
            if self.id_node is None:
                return self.id_node
            if node < self.id_node:
                self.left = self.left.delete(node)
            elif node > self.id_node:
                self.right = self.right.delete(node)
            else:
                if self.left is None:
                    temp = self.right
                    self = None
                    return temp
                elif self.right is None:
                    temp = self.left
                    self = None
                    return temp
                temp = self.right.find_min()
                self.id_node = temp
                self.right = self.right.delete_node(temp)
            return self

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node),
        if self.right:
            self.right.print_tree()