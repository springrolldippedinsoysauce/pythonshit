from DataStructures import Collections


class Vertex:
    def __init__(self, label):
        self.label = label
        self.links = Collections.LinkedList()
        self.visited = False

    def get_label(self):
        return self.label

    def get_adjacent(self):
        return self.links

    def to_string(self):
        string = "{:7}|".format(self.label)
        for v in self.links:
            string += "{} ".format(v.get_label())
        return string

    def add_edge(self, vertex):
        try:
            if self.vertex_present(vertex) is True:
                self.links.insert_last(vertex)
            else:
                raise GraphError("Error: Edge already present!")
        except GraphError:
            pass

    def set_visited(self):
        self.visited = True

    def clear_visited(self):
        self.visited = False

    def get_visited(self):
        return self.visited

    def vertex_present(self, v):
        it_exist = False
        iterator = self.links
        if v is not None:
            for value in iterator:
                if value.get_label() == v:
                    it_exist = True
        return it_exist


class Error(Exception):
    pass


class GraphError(Error):
    def __iter__(self, message):
        self.message = message
