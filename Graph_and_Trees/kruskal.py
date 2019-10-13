# KRUSKAL ALGHORITM
# Used to find the minimum spanning tree -> the tree (graph with no loop) that realizes an hamiltoniam graph on a loop one
# It works considering only edge of graph, since all nodes will be covered (hamiltonian graph)

from Graph_and_Trees.tree import *
from Graph_and_Trees.graph import *

def kruskal(graph):
    sol = []
    partitions = []
    edges = graph.getEdges().copy()

    # stop when all edges have been considered or when we have as much nodes as edges minus one
    while len(edges) > 0 and len(sol)/2 < len(graph.vertexes)-1:
        # get minimum cost edge
        curr = getMinimumCostEdge(edges)
        edges.remove(curr)

        # check for loop
        src_part = getNodeSubPartiton(curr.src, partitions)
        dest_part = getNodeSubPartiton(curr.dest, partitions)

        # UNION FIND Data Structure
        # src and destionation belong to a prtition -> possible loop formation
        # if they are in the same partition, they will create a loop -> do not add
        # if they belong to two partitions now the tow subtrees are connected -> join partitions
        if src_part != None and dest_part != None:
            if src_part != dest_part:
                union = src_part + dest_part
                partitions.remove(src_part)
                partitions.remove(dest_part)
                partitions.append(union)
                sol.append(curr)

                # there is no need to check the opposite link, the alg is designed to work with bidirectional link
                opposite = getOppositeEdge(curr, edges)
                sol.append(opposite)
                edges.remove(opposite)

        elif src_part != None:  # the destination has no partition so add to the source one
            src_part.append(curr.dest)
            # add the link and it's opposite to the solution
            sol.append(curr)
            opposite = getOppositeEdge(curr, edges)
            sol.append(opposite)
            edges.remove(opposite)

        elif dest_part != None:  # same as up but the inverse case
            dest_part.append(curr.src)

            sol.append(curr)
            opposite = getOppositeEdge(curr, edges)
            sol.append(opposite)
            edges.remove(opposite)

        else:  # neither src nd dest belong to a partition so create a new one with both
            partitions.append([curr.src, curr.dest])

            sol.append(curr)
            opposite = getOppositeEdge(curr, edges)
            sol.append(opposite)
            edges.remove(opposite)

        # print status of partitions
        for e in partitions:
            print("[", end='')
            for p in e:
                print(str(p.id), end='')
            print("]", end='')
        print()


    return sol

# get the edge with minimum path cost


def getMinimumCostEdge(edges):
    min = edges[0]
    for e in edges:
        if e.cost < min.cost:
            min = e
    return min

# get the complementar edge


def getOppositeEdge(e, edges):
    for i in edges:
        if e.src == i.dest and e.dest == i.src:
            return i
    return None

# get the subpartition to wich a node belong


def getNodeSubPartiton(node, partitions):
    if len(partitions) == 0:
        return None
    for p in partitions:
        if node in p:
            return p
    return None


# TEST
g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")
g.addVertex("G")

g.addBidirectionalEdge("A", "B", 1)
g.addBidirectionalEdge("A", "F", 7)
g.addBidirectionalEdge("A", "C", 4)

g.addBidirectionalEdge("B", "E", 3)
g.addBidirectionalEdge("B", "D", 8)

g.addBidirectionalEdge("C", "E", 9)
g.addBidirectionalEdge("C", "D", 20)

g.addBidirectionalEdge("D", "F", 2)

g.addBidirectionalEdge("E", "F", 6)

g.addBidirectionalEdge("G", "D", 5)

# g.printGraph()

sol = kruskal(g)
print("Result:")
for e in sol:
    print(str(e.src.id) + " " + str(e.dest.id) + " " + str(e.cost))
