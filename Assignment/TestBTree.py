from Assignment import BlockTree


file = str(input("Enter file name > "))
order = int(input("Enter the order > "))
tree = BlockTree.BlockTree(2, file)
print("===============================================================================================")
print("Tree size: ", tree.get_size())
print("Tree height: ", tree.get_height())
print("Tree ideal height: ", tree.get_ideal_height())
