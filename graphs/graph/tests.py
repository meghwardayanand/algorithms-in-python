import unittest

from graphs.graph.graph import Graph


class TestGraph(unittest.TestCase):

    def test_create_graph_with_invalid_representation(self):
        with self.assertRaises(ValueError):
            Graph(representation='invalid')

    def test_empty_list(self):
        graph = Graph(representation='list')
        self.assertEqual(graph.graph, {})

    def test_empty_matrix(self):
        graph = Graph(representation='matrix')
        self.assertEqual(len(graph.matrix), 0)

    def test_add_vertex_list(self):
        graph = Graph(representation='list')
        graph.addVertex("A")
        self.assertIn("A", graph.graph)
        self.assertEqual(graph.graph["A"], [])

    def test_add_vertex_matrix(self):
        graph = Graph(representation='matrix')
        graph.addVertex("A")
        self.assertIn("A", graph.vertices)
        self.assertEqual(len(graph.matrix), 1)
        self.assertEqual(len(graph.matrix[0]), 1)

    def test_add_edge_list(self):
        graph = Graph(representation='list')
        graph.addEdge("A", "B")
        self.assertIn("A", graph.graph)
        self.assertIn("B", graph.graph)
        self.assertIn("B", graph.graph["A"])
        self.assertIn("A", graph.graph["B"])

    def test_add_edge_matrix(self):
        graph = Graph(representation='matrix')
        graph.addEdge("A", "B")
        self.assertIn("A", graph.vertices)
        self.assertIn("B", graph.vertices)
        index1 = graph.vertices.index("A")
        index2 = graph.vertices.index("B")
        self.assertEqual(graph.matrix[index1][index2], 1)
        self.assertEqual(graph.matrix[index2][index1], 1)

    def test_add_edge_directed(self):
        graph = Graph(representation='list', is_directed=True)
        graph.addEdge("A", "B")
        self.assertIn("B", graph.graph["A"])
        self.assertNotIn("A", graph.graph["B"])

    def test_add_edge_weighted(self):
        graph = Graph(representation='list', is_weighted=True)
        graph.addEdge("A", "B", weight=5)
        graph.addEdge("A", "C", weight=3)
        self.assertIn(("B", 5), graph.graph["A"])
        self.assertIn(("C", 3), graph.graph["A"])

    def test_add_edge_weighted_matrix(self):
        graph = Graph(representation='matrix', is_weighted=True)
        graph.addEdge("A", "B", weight=5)
        graph.addEdge("A", "C", weight=3)
        index1 = graph.vertices.index("A")
        index2 = graph.vertices.index("B")
        index3 = graph.vertices.index("C")
        self.assertEqual(graph.matrix[index1][index2], 5)
        self.assertEqual(graph.matrix[index1][index3], 3)

    def test_remove_vertex_list(self):
        graph = Graph(representation='list')
        graph.addEdge("A", "B")
        graph.addEdge("B", "C")
        graph.removeVertex("B")
        self.assertNotIn("B", graph.graph)
        self.assertNotIn("B", graph.graph["A"])
        self.assertNotIn("B", graph.graph["C"])

    def test_remove_vertex_matrix(self):
        graph = Graph(representation='matrix')
        graph.addEdge("A", "B")
        graph.addEdge("B", "C")
        graph.removeVertex("B")
        self.assertNotIn("B", graph.vertices)
        self.assertEqual(len(graph.matrix), 2)
        self.assertEqual(len(graph.matrix[0]), 2)

    def test_remove_edge_list(self):
        graph = Graph(representation='list')
        graph.addEdge("A", "B")
        graph.addEdge("B", "C")
        graph.removeEdge("A", "B")
        self.assertNotIn("B", graph.graph["A"])
        self.assertNotIn("A", graph.graph["B"])

    def test_remove_edge_matrix(self):
        graph = Graph(representation='matrix')
        graph.addEdge("A", "B")
        graph.addEdge("B", "C")
        graph.removeEdge("A", "B")
        index1 = graph.vertices.index("A")
        index2 = graph.vertices.index("B")
        self.assertEqual(graph.matrix[index1][index2], 0)
        self.assertEqual(graph.matrix[index2][index1], 0)

    def test_repr_list(self):
        graph = Graph(representation='list')
        graph.addEdge("A", "B")
        graph.addEdge("A", "C")
        repr_output = repr(graph)
        self.assertIn("A: ['B', 'C']", repr_output)
        self.assertIn("B: ['A']", repr_output)

    def test_repr_matrix(self):
        graph = Graph(representation='matrix')
        graph.addEdge("A", "B")
        graph.addEdge("A", "C")
        repr_output = repr(graph)
        self.assertIn("Adjacency Matrix:", repr_output)
        self.assertIn("A 0 1 1", repr_output)
        self.assertIn("B 1 0 0", repr_output)

    def test_edge_and_vertex_consistency_list(self):
        graph = Graph(representation='list')
        graph.addEdge("A", "B")
        graph.addEdge("B", "C")
        self.assertIn("A", graph.graph)
        self.assertIn("B", graph.graph)
        self.assertIn("C", graph.graph)
        self.assertIn("B", graph.graph["A"])
        self.assertIn("C", graph.graph["B"])

    def test_edge_and_vertex_consistency_matrix(self):
        graph = Graph(representation='matrix')
        graph.addEdge("A", "B")
        graph.addEdge("B", "C")
        self.assertIn("A", graph.vertices)
        self.assertIn("B", graph.vertices)
        self.assertIn("C", graph.vertices)
        index1 = graph.vertices.index("A")
        index2 = graph.vertices.index("B")
        index3 = graph.vertices.index("C")
        self.assertEqual(graph.matrix[index1][index2], 1)
        self.assertEqual(graph.matrix[index2][index3], 1)

    def test_remove_edge_directed(self):
        graph = Graph(representation='list', is_directed=True)
        graph.addEdge("A", "B")
        graph.addEdge("B", "C")
        graph.removeEdge("A", "B")
        self.assertNotIn("B", graph.graph["A"])
        self.assertIn("C", graph.graph["B"])

    def test_remove_edge_weighted(self):
        graph = Graph(representation='list', is_weighted=True)
        graph.addEdge("A", "B", weight=10)
        graph.addEdge("A", "C", weight=5)
        graph.removeEdge("A", "B")
        self.assertNotIn(("B", 10), graph.graph["A"])
        self.assertIn(("C", 5), graph.graph["A"])

    def test_remove_edge_weighted_matrix(self):
        graph = Graph(representation='matrix', is_weighted=True)
        graph.addEdge("A", "B", weight=10)
        graph.addEdge("A", "C", weight=5)
        graph.removeEdge("A", "B")
        index1 = graph.vertices.index("A")
        index2 = graph.vertices.index("B")
        self.assertEqual(graph.matrix[index1][index2], 0)
        self.assertEqual(graph.matrix[index2][index1], 0)


if __name__ == '__main__':
    unittest.main()
