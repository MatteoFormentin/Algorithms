import unittest
from Graph_and_Trees.tree import *
from Graph_and_Trees.bfs import *
from Graph_and_Trees.dfs import *


class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = Tree("A")
        self.tree.addChild("A", "B")
        self.tree.addChild("A", "C")
        self.tree.addChild("A", "D")

        self.tree.addChild("B", "E")
        self.tree.addChild("E", "F")

    def test_bfs(self):
        res = bfs(self.tree, "A")
        t = []
        for i in res:
            t.append(i.id)
        self.assertEqual(t, ["A", "B", "C", "D", "E", "F"])

    def test_dfs(self):
        res = dfs(self.tree)
        t = []
        for i in res:
            t.append(i.id)
        self.assertEqual(t, ['F', 'E', 'B', 'C', 'D', 'A'])


if __name__ == '__main__':
    unittest.main()
