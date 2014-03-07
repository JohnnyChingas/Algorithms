# Graph using adjacency lists
# T. Melano

from collections import deque

MAXV = 100

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


def print_graph(graph):
    """
    @param graph: Graph object
    """
    for i in xrange(1,graph.nvertices+1):
        print "%d:\n"%i,
        p = graph.edges[i]
        while p != None:
            print " %d"%p.y
            p = p.next
        print "\n"


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


# Breadth First Search methods
# Global variables
processed = [None]*MAXV # boolean list of which vertices have been processed
discovered = [None]*MAXV # boolean list of which vertices have been found
parent = [None]*MAXV # integer list of discovery relation

def initialize_bfs_search(graph):
    for i in xrange(1,graph.nvertices+1):
        processed[i] = discovered[i] = False
        parent[i] = -1 # the parent of vertex i is parent[i]

def bfs(graph, start):
    # Run time O(n vertices + m edges)
    # First node is processed immediately
    # The vertices that follow are first discovered, added to queue of vertices to process
    #       then transition to processed once the are popped from the queue
    # The queue is FIFO


    q = deque([]) # queue of vertices to visit

    q.append(start) 
    discovered[start] = True

    while len(q) != 0:
        v = q.popleft()
        process_vertex_early(v) # illustrative 
        processed[v] = True
        p = graph.edges[v]
        while p != None:
            y = p.y
            if (discovered[y] == False):
                appending_vertex(y) # illustrative 
                q.append(y)
                discovered[y] = True
                parent[y] = v
            if ((processed[y] == False) or graph.directed):
                process_edge(v,y) # illustrative 
            p = p.next
        process_vertex_late(v) # illustrative 
    return parent

def process_vertex_late(v):
    return True

def process_vertex_early(v):
    print "processed vertex %d\n"%v

def process_edge(x,y):
    print "processed edge (%d,%d)\n"%(x,y)

def appending_vertex(v):
    print "appending vertex %d to queue\n"%v

def find_path(start,end,parents):
    if start == end or end == -1:
        print start,
    else:
        find_path(start,parents[end],parents)
        print end,

def connected_components(graph):
    # count the number of connected components in a graph

    initialize_bfs_search(graph)
    
    c = 0 # Component number 

    for i in xrange(1,graph.nvertices+1):
        if discovered[i] == False:
            c += 1
            bfs(graph,i)
            print "Component %d"%c

# Depth First Search methods
# Global variables
finished = False
time = 0

def initialize_dfs_search(graph):
    finished = False
    time = 0
    for i in xrange(1,graph.nvertices+1):
        processed[i] = discovered[i] = False
        parent[i] = -1 # the parent of vertex i is parent[i]
        entry_time[i] = exit_time[i] = None

def dfs(graph,v):
    if finished: #allow for search termination
        return
    discovered[v] = True
    time = time + 1
    entry_time[v] = time

    process_vertex_early_dfs(v)

    p = graph.edges[v]
    while p != None:
        y = p.y
        if discovered[y] == False:
            parent[y] = v
            process_edge_dfs(v,y)
            dfs(graph,y)
        elif not processed[y] or graph.directed:
            process_edge_dfs(v,y)
        if finished:
            return
        p = p.next

    process_vertex_late_dfs(v)

    time = time +1
    exit_time[v] = time

    processed[v] = True

def main():
    graph = Graph()
    read_graph(graph, False)
    print_graph(graph)
    start = 1
    end = 4
    initialize_bfs_search(graph)
    parent = bfs(graph,start)

    print "Path from %d to %d"%(start,end)
    find_path(start,end,parent)

    print "Find connected components"
    connected_components(graph)


if __name__ == "__main__":
    main()
