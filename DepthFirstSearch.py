# Depth First Search methods
# Global variables

MAXV = 7
processed = [None]*MAXV # boolean list of which vertices have been processed
discovered = [None]*MAXV # boolean list of which vertices have been found
parent = [None]*MAXV # integer list of discovery relation
finished = False
entry_time = [None]*MAXV
exit_time = [None]*MAXV
time = 0

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
    @param graph: Graph object
    @param directed: boolean
    """
    graph.nvertices = 0
    graph.nedges = 0
    graph.directed = directed

    for i in xrange(MAXV):
        graph.degree.append(0)
        graph.edges.append(None)

def read_graph(graph, directed):
    """
    @param graph: Graph object
    @param directed: boolean
    """
    initialize_graph(graph, directed)
    data = graph_data()
    
    graph.nvertices = data[0][0] # number of vertices
    m = data[0][1] # number of edges

    for i in xrange(1,m+1):
        x = data[i][0] # vertex x
        y = data[i][1] # vertex y
        insert_edge(graph,x,y,directed)

def insert_edge(graph, x, y, directed):
    """
    @param graph: Graph object
    @param x, y: vertices in edge (x,y)
    @param directed: boolean
    """
    p = Edgenode()
    p.y = y
    p.next = graph.edges[x] #p.next point to whatever is in edges[x] 

    graph.edges[x] = p #edges[x], gets replaced by the new p, which points to whatever was in edges[x] before

    graph.degree[x] += 1

    if (directed == False):
        insert_edge(graph, y, x, True)
    else:
        graph.nedges += 1

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

def initialize_search(graph):
    finished = False
    for i in xrange(1,graph.nvertices+1):
        processed[i] = discovered[i] = False
        parent[i] = -1 # the parent of vertex i is parent[i]
        entry_time[i] = exit_time[i] = None

def dfs(graph,v):
    global time
    if finished: #allow for search termination
        return
    discovered[v] = True
    time = time + 1
    entry_time[v] = time

    process_vertex_early(v)

    p = graph.edges[v]
    while p != None:
        y = p.y
        if discovered[y] == False:
            parent[y] = v
            process_edge(v,y)
            dfs(graph,y)
        elif not processed[y] or graph.directed:
            process_edge(v,y)
            True
        if finished:
            return
        p = p.next

    process_vertex_late(v)

    time = time + 1
    exit_time[v] = time

    processed[v] = True

def process_vertex_early(v):
    print "Discovered vertex %d\n"%v

def process_edge(x,y):
    print "Processed edge (%d,%d)\n"%(x,y)

def process_vertex_late(v):
    print "Processed vertex %d\n"%v

def main():
    graph = Graph()
    read_graph(graph, False)
    start = 1
    initialize_search(graph)
    dfs(graph,start)

    for i in xrange(1,graph.nvertices+1):
        print "Entry time for vertix %d: %d"%(i,entry_time[i])
        print "Exit time for vertix %d: %d\n"%(i,exit_time[i])

if __name__ == "__main__":
    main()
