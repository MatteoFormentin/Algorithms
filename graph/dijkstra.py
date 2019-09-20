# Dijkstra Algorithm
#
# Used for know the best route from one start vertex to all the others
# How it works: first, each node is assigned a label which contains the cost to be reached and the precedent node for the path
# then for each node their adjacent are examinated (apart prec node) and the reach cost is updated with path cost plus the labeled total one.
# If the adj nodes has not infinite as label it is check if new reach cost is minor. When visited, each node is moved in a visited list, then
# it is choosed the node not already visited with minimum total cost label as next to be examineted.
# I choose the min since else i can't examinate path other then the direct one since the algorithm explore only not visited adjacent.
# When to visit list is empty or all nodes in to be visited have infinite has cost stop.

from graph import *


class NodeLabelWrapper():
    def __init__(self, node):
        self.node = node
        self.prec = None
        self.path_cost = -1


def dijkstra(g, start_id):  # Note that graph is of my costum graph implementation, start is the friendly identifier

    vertex = g.vertexes
    # Init -> all nodes have infinite cost (-1) and no prec node
    nodes = [NodeLabelWrapper(v) for v in vertex]  # not visited
    not_visited = nodes.copy()
    visited = []  # visited and correctly labeled

    start_node = getLabeledNodeById(start_id, nodes)
    start_node.path_cost = 0

    while len(not_visited) > 0:  # continue while all nodes are visited or remaining are unreachable
        if len(visited) == 0:  # first interaction -> we start from start node
            n = start_node
        else:
            # take the smalles total path distance as next node to visit
            n = getMinLabeledNodePathCost(not_visited)
            if n.path_cost == -1:  # if min is infinite, all nodes remaining are unreachable, so break
                break

        # move node to visited list
        visited.append(n)
        not_visited.remove(n)

        # update all adjacent nodes of n
        for e in n.node.edges:
            curr = getLabeledNodes(e.dest, nodes)
            # Check only node not visited -> they have i cant go to that nodes from starting one passing to this one
            if not curr in visited:
                # Cost to reach next is cost to reach prec + path between cost
                to_curr_path_cost = n.path_cost + e.cost
                # set n as path to adjacent only if its path cost its smaller than actual
                if curr.path_cost == -1 or to_curr_path_cost < curr.path_cost:
                    curr.path_cost = to_curr_path_cost
                    curr.prec = n

    # Print result
    for n in visited:
        print(str(n.node.id) + "  " + str(n.path_cost))


def getLabeledNodeById(id, labeled_list):
    for n in labeled_list:
        if id == n.node.id:
            return n
    return None

# Utils to get a NodeLabelWapper from a list from its corresponding vertex


def getLabeledNodes(node, labeled_list):
    for n in labeled_list:
        if node is n.node:
            return n
    return None


def getMinLabeledNodePathCost(labeled_list):
    min = labeled_list[0]
    for n in labeled_list:
        if min.path_cost == -1 or n.path_cost != -1 and n.path_cost < min.path_cost:
            min = n
    return min


# TEST
g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addBidirectionalEdge("A", "B", 3)
g.addBidirectionalEdge("A", "C", 2)
g.addBidirectionalEdge("B", "C", 10)
g.addBidirectionalEdge("B", "D", 2)
g.addBidirectionalEdge("C", "D", 2)
g.printGraph()

print()

dijkstra(g, "A")
