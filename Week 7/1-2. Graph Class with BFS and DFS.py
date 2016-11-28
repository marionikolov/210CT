class Graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self, node):
        newVertex = Vertex(node)
        self.vertices[node] = newVertex

    def addEdge(self, node1, node2):
        if node1 not in self.vertices:
            self.addVertex(node1)
        if node2 not in self.vertices:
            self.addVertex(node2)
        self.vertices[node1].addAdjacent(node2)
        self.vertices[node2].addAdjacent(node1)

    def __str__(self):
        return str([str(x) for x in self.vertices.values()])

class Vertex:
    def __init__(self, label):
        self.label = label
        self.adjacent = []

    def addAdjacent(self, node):
        self.adjacent.append(node)

    def __str__(self):
        return str(self.label) + ": " + str([x for x in self.adjacent])

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