from Graphs import Graph


file = str(input("Enter the name of the file to be graphed > "))
graph = Graph.Graph(file)
print(graph.display_list())
