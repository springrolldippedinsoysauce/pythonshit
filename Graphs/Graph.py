from DataStructures import Collections


class Vertex:
    def __init__(self, label: str):
        self.label = label
        self.adjacency_list = Collections.LinkedList()
        self.visited = False

    def adjacency_matrix_row(self, vertex_list):
        row = []
        for v in vertex_list:
            row.append(1 if self.present(v.label) else 0)
        return row

    def present(self, label: str):
        present = False
        for e in self.adjacency_list:
            if e.label == label:
                present = True
                break
        return present

    def add_edge(self, vertex):
        if not Vertex.present(self, vertex.label):
            self.adjacency_list.insert_last(vertex)
        else:
            raise GraphError("Error: Edge already present")

    def to_string(self):
        string = "{:7}|".format(self.label)
        for v in self.adjacency_list:
            string += "{} ".format(v.label)
        return string


class Graph:
    def __init__(self, filename):
        self.vertex_list = Collections.LinkedList()
        self.vertex_count = 0
        self.edge_count = 0
        with open(filename, 'r') as f:
            vertices = f.read().split('\n')
            print(len(vertices))
        for v in vertices:
            edge = v.split(' ')
            if len(edge) == 2:
                print(edge)
                if not Graph.vertex_present(self, edge[0]):
                    self.vertex_list.insert_last(Vertex(edge[0]))
                if not Graph.vertex_present(self, edge[1]):
                    self.vertex_list.insert_last(Vertex(edge[1]))
                Graph.add_edge(self, edge[0], edge[1])
            else:
                if len(edge) > 1:
                    raise GraphError("Invalid file format")

    def __str__(self):
        self.adjacency_matrix = []

    def vertex_present(self, label: str):
        present = False
        for v in self.vertex_list:
            if v.label == label:
                present = True
                break
        return present

    def find_vertex(self, label):
        vertex = None
        for v in self.vertex_list:
            if v.label == label:
                vertex = v
                break
        return vertex

    def add_edge(self, label_one, label_two):
        if Graph.vertex_present(self, label_one) and Graph.vertex_present(self, label_two):
            v1 = Graph.find_vertex(self, label_one)
            v2 = Graph.find_vertex(self, label_two)
            v1.add_edge(v2)
            self.edge_count += 1
        else:
            raise GraphError("One or more of the passed vertices are not present")

    def display_list(self):
        table = "Vertex |Adjacent\n"
        for v in self.vertex_list:
            table += v.to_string() + "\n"
        return table


class Error(Exception):
    pass


class GraphError(Error):
    def __iter__(self, message):
        self.message = message
