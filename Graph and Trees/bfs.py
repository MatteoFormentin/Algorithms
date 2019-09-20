# BFS (Breadth-First Search) ALGORITHM
# Visit all nodes starting from adjacent then going deep. All node are white colored, when first visited grey colored
# and finally when all adjacent has been visited black colored
# Nodes are marked as grey since in a cyclic graph they can be already been visited

from tree import *
from graph import *


def bfs(graph, root_id):
    white = [x for x in graph.vertexes]
    grey = []
    black = []
    queue = []

    root = graph.getNodeById(root_id)
    white.remove(root)
    grey.append(root)
    # When grey colored each node is inserted in queue, then one is FIFO extracted and their children are grey colored
    # at the beginning only root is in queue, so it will be the first to be examineted
    queue.append(root)

    while len(queue) > 0:
        curr = queue.pop(0)  # Get another node to examneted
        print(curr.id)
        for e in curr.edges:
            if e.dest in white:
                # Grey color all children
                white.remove(e.dest)
                grey.append(e.dest)
                queue.append(e.dest)
        # mark this node as visited (black) and go to the next
        grey.remove(curr)
        black.append(curr)


# TEST
t = Tree("A")
t.addChild("A", "B")
t.addChild("A", "C")
t.addChild("A", "D")

t.addChild("B", "E")
t.addChild("E", "F")
t.printGraph()
bfs(t, "A")
