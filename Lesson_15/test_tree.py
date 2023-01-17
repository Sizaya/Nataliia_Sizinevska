from Tree import Tree

def test_add_elements():
    test_tree = Tree(7)
    test_tree2 = Tree(7)
    test_tree2.right = Tree(12)
    test_tree2.right.right = Tree(12)
    test_tree.add_elements([11, 17])
    assert test_tree2.id_node == test_tree.id_node
    assert test_tree2.right.id_node == test_tree.right.id_node
    assert test_tree2.right.right.id_node == test_tree.right.right.id_node

def test_min_element():
    test_tree = Tree(7)
    test_tree.add_elements([11, 5, 2])
    assert test_tree.min() == 2


def test_max_element():
    test_tree = Tree(5)
    test_tree.add_elements([11, 5, 2])
    assert test_tree.max() == 11


def test_delete_element():
    test_tree = Tree(5)
    test_tree.add_elements([11, 5, 4, 1, 2, 10])
    test_tree.delete(3)
    assert test_tree.left.id_node == 4