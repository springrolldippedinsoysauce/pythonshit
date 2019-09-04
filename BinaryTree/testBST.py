from BinaryTree import BST

my_tree = BST.BinarySearchTree()

my_tree.display()

my_tree.insert(5, "five")
my_tree.insert(6, "six")
my_tree.insert(3, "three")
my_tree.insert(8, "eight")
my_tree.insert(2, "two")
my_tree.insert(9, "nine")
my_tree.insert(7, "seven")

my_tree.display()

print(my_tree.find(9))
