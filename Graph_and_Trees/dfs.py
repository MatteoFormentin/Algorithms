# DFS (Depth-First Search) ALGORITHM
# Visit all nodes starting deep then adjacent (each connection is followed until it ends). All node are white colored, when first visited grey colored
# and finally when all adjacent nodes has been visited are black colored
# Nodes are marked as grey since in a cyclic graph they can be already been visited


from Graph_and_Trees.tree import *
from Graph_and_Trees.graph import *


def dfs(graph):
    # Initialization -> all node are white colored
    white = [x for x in graph.vertexes]
    grey = []
    black = []
    for n in graph.vertexes: #cycle is needed in case one node is not accesible from the root (single direction link)
        if n in white:
            dfs_visit(n, white, grey, black)
    return black


def dfs_visit(n, white, grey, black):
    #mark current as grey
    white.remove(n)
    grey.append(n)

    # foreach adjacent node of n, go deep recursivly
    for e in n.edges:
        if e.dest in white:
            # when return, next n child ramification will be examinated
            dfs_visit(e.dest, white, grey, black)
    grey.remove(n)  # ramification end -> color black
    black.append(n)