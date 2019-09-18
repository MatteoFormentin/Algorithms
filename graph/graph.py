
# GRAPH
# A Series of Vertexes (nodes) connected by Edges (paths)


class Vertex():
    def __init__(self, id):
        self.id = id
        self.edges = []

    # Connect to an adjacent Vertex
    def addEdge(self, dest, cost=0):
        self.edges.append(Edge(self, dest, cost))

# Define a directional link between two nodes.
# Note: to make the link bidirectional one edge per Vertex is required.


class Edge():
    def __init__(self, src, dest, cost=0):
        self.src = src
        self.dest = dest
        self.cost = cost

# TODO: Adjacent matrix import-export
class Graph():
    def __init__(self):
        self.vertexes = []

    # Add new Vertex to the graph, id is a friendly identifier
    def addVertex(self, id):
        new = Vertex(id)
        self.vertexes.append(new)

    # define a new symmetrical connection between two Vertex (selected by friendly id)
    def addBidirectionalEdge(self, a_id, b_id, cost=0):
        if a_id != b_id:  # Cannot connect Vertex with itself TODO: EMPTY - ONE ELEMENT, link exist, multiple cost...
            a = None
            b = None
            for v in self.vertexes: #search vertex to connect by id
                if v.id == a_id:
                    a = v
                if v.id == b_id:
                    b = v

            if a and b != None:
                a.addEdge(b, cost)
                b.addEdge(a, cost)
                return True

        return False

    def getSize():
        return len(self.vertexes)

    def printGraph(self):
        for v in self.vertexes:
            print(v.id, "")
            for e in v.edges:
                print("->" + str(e.dest.id + "(" + str(e.cost) + ")"), "")

#TEST
g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addBidirectionalEdge("A", "B")
g.addBidirectionalEdge("A", "C")
g.addBidirectionalEdge("A", "D")
g.addBidirectionalEdge("B", "C")
g.addBidirectionalEdge("B", "D")
g.printGraph()
