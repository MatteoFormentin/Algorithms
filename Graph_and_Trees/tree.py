# TREE DATA STRUCTURE
# General unordered tree implementation, rely on graph class (tree is just an acyclic graph)
from Graph_and_Trees.graph import *

class Tree(Graph):
    def __init__(self, root_id):
        super().__init__()
        self.root = self.addVertex(root_id)

    def addChild(self, parent, new_node_id):
        self.addVertex(new_node_id)
        self.addBidirectionalEdge(new_node_id, parent, cost=0)

    def getRoot(self):
        return self.vertexes[0]

    def deleteNode(self, node_id):  #  TODO:finish
        d = self.getNodeById(node_id)
        if d == None:
            return False

        for e in d.edges:
            e.dest
