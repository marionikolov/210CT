class Graph:
    """
    Instantiates an undirected unweighted graph. Call empty and then fill in using the addVertex and addEdge methods.
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
    Adds a new edge between two vertices. If the vertices have not yet been added to the graph, the function will automatically add them.
    """
    def addEdge(self, node1, node2):
        if node1 not in self.vertices:
            self.addVertex(node1)
        if node2 not in self.vertices:
            self.addVertex(node2)
        self.vertices[node1].addAdjacent(node2)
        self.vertices[node2].addAdjacent(node1)

    def __str__(self):
        return str([str(x) for x in self.vertices.values()]) # uses list comprehension to print all the vertices

class Vertex:
    """
    Used by the Graph() class to instantiate vertices and keep a record of their edges. Create vertices only through the Graph() class's addVertex() method.
    """
    def __init__(self, label):
        self.label = label # the value of the vertex
        self.adjacent = [] # list of all adjacent vertices references by their value

    def addAdjacent(self, node):
        self.adjacent.append(node)

    def __str__(self):
        return str(self.label) + ": " + str([x for x in self.adjacent]) # uses list comprehension to print all the adjacent vertices

if __name__ == '__main__':
    graph1 = Graph()
    graph1.addVertex(1)
    graph1.addVertex(2)
    graph1.addVertex(3)
    graph1.addVertex(4)

    graph1.addEdge(1, 2)
    graph1.addEdge(1, 3)
    graph1.addEdge(2, 3)
    graph1.addEdge(3, 4)
    graph1.addEdge(2, 4)

    print(graph1)