from queue import Queue
import math

class WeightedGraph:
    """
    Instantiates an undirected weighted graph. Call empty and then fill in using the addVertex and addEdge methods.
    Example: graph = Graph()
             graph.addVertex(1)
             graph.addVertex(2)
             graph.addEdge(1, 2)
    """

    def __init__(self):
        self.vertices = {} # Used to hold references of each vertex through its value for easier access.

    """
    Adds a new vertex to the graph by instantiating a Vertex() object and then adding a reference to its label in the reference dictionary.
    """
    def addVertex(self, node):
        newVertex = Vertex(node)
        self.vertices[node] = newVertex

    """
    Adds a new edge between two vertices and its weight. If the vertices have not yet been added to the graph, the function will automatically add them.
    """
    def addEdge(self, node1, node2, weight):
        if node1 not in self.vertices:
            self.addVertex(node1)
        if node2 not in self.vertices:
            self.addVertex(node2)
        self.vertices[node1].addAdjacent(node2, weight)
        self.vertices[node2].addAdjacent(node1, weight)

    """
    Traverses the graph by visiting each vertex in turn starting with the input start vertex.
    """
    def DFS(self, start):
        stack = []
        visited = []
        stack.append(start)
        while len(stack) > 0:
            u = stack.pop()
            if u not in visited:
                for e in self.vertices[u].adjacent:
                    stack.append(e)
                visited.append(u)
        file = open("DFSresult.txt", "w")
        file.write(str(visited))
        file.close()

    """
    Traverses the graph by searching every edge from the input start vertex.
    """
    def BFS(self, start):
        q = Queue()
        visited = []
        q.put(start)
        while q.qsize() > 0:
            u = q.get()
            if u not in visited:
                for e in self.vertices[u].adjacent:
                    q.put(e)
                visited.append(u)
        file = open("BFSresult.txt", "w")
        file.write(str(visited))
        file.close()

    """
    """
    def Dijkstra(self, source, destination):
        source = self.vertices[source] # get the actual Vertex() object
        destination = self.vertices[destination]

        source.tentativeWeight = 0 # the souce is at distance 0 from itself
        v = source # currently scanned vertex
        visited = []

        while v != destination:
            for u in v.adjacent.keys():
                u = self.vertices[u] # see whether i can remove that
                if v.tentativeWeight + v.adjacent[u.label] < u.tentativeWeight:
                    u.tentativeWeight = v.tentativeWeight + v.adjacent[u.label]
                    u.pre = v # store the return path

            visited.append(v)
            minimum = math.inf

            for n in self.vertices.values():
                if n not in visited and n.tentativeWeight < minimum:
                    v = n
                    minimum = n.tentativeWeight
        return v.tentativeWeight

    def __str__(self):
        return str([str(x) for x in self.vertices.values()]) # uses list comprehension to print all the vertices

class Vertex:
    """
    Used by the Graph() class to instantiate vertices and keep a record of their edges. Create vertices only through the Graph() class's addVertex() method.
    """
    def __init__(self, label):
        self.label = label # the value of the vertex
        self.adjacent = {} # dictionary of all adjacent vertices; key: vertex label, value: weight of edge
        self.tentativeWeight = math.inf # tentative weight used for Dijkstra's algorithm; default value is infinity
        self.pre = None # return path used for Dijkstra's algorithm

    def addAdjacent(self, node, weight):
        self.adjacent[node] = weight

    """
    Returns a string version of the vertex and all its edges in the format vertex: [(edge1, weight1), (edge2, weight2)]
    """
    def __str__(self):
        return str(self.label) + ": " + str([(x, k) for x,k in self.adjacent.items()]) # uses list comprehension to print all the adjacent vertices and the weight of the edges connceting them

if __name__ == '__main__':
    graph1 = WeightedGraph()
    graph1.addVertex(1)
    graph1.addVertex(2)
    graph1.addVertex(3)
    graph1.addVertex(4)
    graph1.addVertex(5)
    graph1.addVertex(6)
    graph1.addVertex(7)
    graph1.addVertex(8)

    graph1.addEdge(1, 2, 4)
    graph1.addEdge(1, 3, 6)
    graph1.addEdge(2, 3, 7)
    graph1.addEdge(3, 4, 3)
    graph1.addEdge(2, 4, 10)
    graph1.addEdge(4, 5, 10)
    graph1.addEdge(5, 6, 9)
    graph1.addEdge(6, 7, 5)
    graph1.addEdge(7, 8, 10)
    graph1.addEdge(6, 8, 9)

    print(graph1)

    DFSresult = graph1.DFS(2)
    BFSresult = graph1.BFS(2)

    res = graph1.Dijkstra(1,8)
    print(res)
