from node import Node

inorder_list = []
preorder_list = []
postorder_list = []

class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ Method for get root of the tree """
        return self.root

    def add(self, data):
        """ Method for add data to the tree """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """Method for add data to the tree

        Args:
            data (int): data to add

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """Method for find data in the tree

        Args:
            data (int): data to find

        Returns:
            Node: node with data
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        self.root = None

    def printTreeInorder(self):
        if self.root is not None:
            self._printInorderTree(self.root)
        print("Inorder: ", inorder_list)

    def printTreePreorder(self):
        if self.root is not None:
            self._printPreorderTree(self.root)
        print("Preorder: ", preorder_list)

    def printTreePostorder(self):
        if self.root is not None:
            self._printPostorderTree(self.root)
        print("Postorder: ", postorder_list)

    def _printInorderTree(self, node):
        if node is not None:
            self._printInorderTree(node.left)
            inorder_list.append(node.data)
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        # TODO
        if node is not None:
            preorder_list.append(node.data)
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        # TODO
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            postorder_list.append(node.data)

def setup_tree():
    tree = Tree()
    tree.add(3)
    tree.add(4)
    tree.add(0)
    tree.add(8)
    tree.add(2)

    inorder_list.clear()
    preorder_list.clear()
    postorder_list.clear()

    return tree

def test_inorder():
    tree = setup_tree()
    tree.printTreeInorder()
    assert inorder_list == [0, 2, 3, 4, 8]

def test_preorder():
    tree = setup_tree()
    tree.printTreePreorder()
    assert preorder_list == [3, 0, 2, 4, 8]

def test_postoder():
    tree = setup_tree()
    tree.printTreePostorder()
    assert postorder_list == [2, 0, 8, 4, 3]

def test_find_existing():
    tree = setup_tree()
    node = tree.find(2)

    assert node is not None
    assert node.data == 2

def test_find_non_existing():
    tree = setup_tree()
    node = tree.find(10)

    assert node is None
