import unittest
from Graph_and_Trees.graph import *
from Graph_and_Trees.tree import *

class TestGraphTree(unittest.TestCase):

    def test_binary_search(self):
        t = Tree("A")
        t.addChild("A", "B")
        t.addChild("A", "C")
        t.addChild("A", "D")

        t.addChild("B", "E")
        t.addChild("E", "F")
        t.printGraph()
        bfs(t, "A")


if __name__ == '__main__':
    unittest.main()
