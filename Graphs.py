# Graph using adjacency lists
# T. Melano

MAXV = 1000

class Edgenode:
    def __init__(self, y = None, weight = None, next = None):
        """
        @param y: adjacency info
        @param weight: edge weight, if any
        @param next: next edge in list
        """
        self.y = y
        self.weight = weight
        self.next = next

class Graph:
    def __init__(self, edges = [], degree = [], nvertices = None, \
                nedges = None, directed = None):
        """
        @param edges: adjency info
        @param degree: outdegree of each vertex
        @param nvertices: number of vertices in graph
        @param nedges: number of edges in graph
        @param directed: is the graph directed? (boolean)
        """
        self.edges = edges # this might be a dictionary, with key being vertex and values being edges
        self.degree = degree
        self.nvertices = nvertices
        self.nedges = nedges
        self.directed = directed


def initialize_graph(graph, directed):
    """
    @param: graph is Graph object
    @param: directed is a boolean
    """
    graph.nvertices = 0
    graph.nedges = 0
    graph.directed = directed

    for i in xrange(MAXV):
        graph.degree[i] = 0
        graph.edges[i] = None

def graph_data():
    data = [
            (6,7),
            (1,2),
            (1,6),
            (1,5),
            (2,3),
            (2,5),
            (5,4),
            (3,4)]
    return data

