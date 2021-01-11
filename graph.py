class Graph:

    def __init__(self):
        self._adjacency_list = {}  # a dictionary

# Adds a new node to the graph
    def add_node(self, value):
        vertex = Vertex(value)
        # adds the key/vertex to the _adjacency_list
        self._adjacency_list[vertex] = []
        return vertex


# Adds a new edge between two nodes in the graph

    def add_edge(self, start_vertex, end_vertex, weight=0):

        # Both nodes should already be in the Graph
        if start_vertex not in self._adjacency_list:
            raise KeyError("Start Vertex not in graph")
        if end_vertex not in self._adjacency_list:
            raise KeyError("End Vertex not in graph")

        edge = Edge(end_vertex, weight)
        adjacencies = self._adjacency_list[start_vertex]
        adjacencies.append(edge)


# Returns all of the nodes in the graph as a collection

    def get_nodes(self):
        return self._adjacency_list.keys()


# Returns a collection of edges connected to the given node
# Include the weight of the connection in the returned collection

    def get_neighbors(self, vertex):
        return self._adjacency_list[vertex]


# Returns the total number of nodes in the graph

    def size(self):
        # returns all the keys in the dict (aka the verticies)
        return len(self._adjacency_list)


# AKA a Node
class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
