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

    def test_bfs_empty_graph(self):
        graph = Graph(representation='list')
        with self.assertRaises(ValueError):
            graph.bfs("A")

    def test_bfs_single_vertex(self):
        graph = Graph(representation='list')
        graph.addVertex("A")
        distances, parents = graph.bfs("A")
        self.assertEqual(distances, {"A": 0})
        self.assertEqual(parents, {"A": None})

    def test_bfs_unweighted_graph(self):
        graph = Graph(representation='list')
        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("C")
        graph.addEdge("A", "B")
        graph.addEdge("A", "C")
        distances, parents = graph.bfs("A")

        self.assertEqual(distances, {"A": 0, "B": 1, "C": 1})
        self.assertEqual(parents, {"A": None, "B": "A", "C": "A"})

    def test_bfs_weighted_graph(self):
        graph = Graph(representation='list', is_weighted=True)
        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("C")
        graph.addEdge("A", "B", weight=5)
        graph.addEdge("A", "C", weight=3)
        distances, parents = graph.bfs("A")

        self.assertEqual(distances, {"A": 0, "B": 5, "C": 3})
        self.assertEqual(parents, {"A": None, "B": "A", "C": "A"})

    def test_bfs_directed_graph(self):
        graph = Graph(representation='list', is_directed=True)
        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("C")
        graph.addEdge("A", "B")
        graph.addEdge("B", "C")
        distances, parents = graph.bfs("A")

        self.assertEqual(distances, {"A": 0, "B": 1, "C": 2})
        self.assertEqual(parents, {"A": None, "B": "A", "C": "B"})

    def test_bfs_disconnected_graph(self):
        graph = Graph(representation='list')
        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("C")
        graph.addVertex("D")
        graph.addEdge("A", "B")
        graph.addEdge("C", "D")
        distances, parents = graph.bfs("A")

        self.assertEqual(distances, {"A": 0, "B": 1, "C": float('inf'), "D": float('inf')})
        self.assertEqual(parents, {"A": None, "B": "A", "C": None, "D": None})

    def test_bfs_matrix_representation(self):
        graph = Graph(representation='matrix')
        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("C")
        graph.addEdge("A", "B")
        graph.addEdge("A", "C")
        distances, parents = graph.bfs("A")

        self.assertEqual(distances, {"A": 0, "B": 1, "C": 1})
        self.assertEqual(parents, {"A": None, "B": "A", "C": "A"})

    def test_bfs_directed_graph_matrix(self):
        graph = Graph(representation='matrix', is_directed=True)
        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("C")
        graph.addEdge("A", "B")
        graph.addEdge("B", "C")
        distances, parents = graph.bfs("A")

        self.assertEqual(distances, {"A": 0, "B": 1, "C": 2})
        self.assertEqual(parents, {"A": None, "B": "A", "C": "B"})

    def test_bfs_nonexistent_vertex(self):
        graph = Graph(representation='list')
        graph.addVertex("A")
        with self.assertRaises(ValueError):
            graph.bfs("B")

    def test_bfs_unreachable_vertices(self):
        graph = Graph(representation='list')
        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("C")
        graph.addEdge("A", "B")
        distances, parents = graph.bfs("A")

        self.assertEqual(distances, {"A": 0, "B": 1, "C": float('inf')})
        self.assertEqual(parents, {"A": None, "B": "A", "C": None})

    def test_dfs_empty_graph(self):
        graph = Graph(representation='list')
        with self.assertRaises(ValueError):
            graph.dfs("A")

    def test_dfs_single_vertex(self):
        graph = Graph(representation='list')
        graph.addVertex("A")
        discovery_time, finishing_time, parents = graph.dfs("A")
        self.assertEqual(discovery_time, {"A": 1})
        self.assertEqual(finishing_time, {"A": 2})
        self.assertEqual(parents, {"A": None})

    def test_dfs_simple_graph_list(self):
        graph = Graph(representation='list')
        graph.addEdge("A", "B")
        graph.addEdge("A", "C")
        graph.addEdge("B", "D")
        discovery_time, finishing_time, parents = graph.dfs("A")
        self.assertEqual(parents, {"A": None, "B": "A", "C": "A", "D": "B"})
        self.assertGreater(finishing_time["B"], discovery_time["B"])
        self.assertGreater(finishing_time["C"], discovery_time["C"])
        self.assertGreater(finishing_time["D"], discovery_time["D"])

    def test_dfs_simple_graph_matrix(self):
        graph = Graph(representation='matrix')
        graph.addEdge("A", "B")
        graph.addEdge("A", "C")
        graph.addEdge("B", "D")
        discovery_time, finishing_time, parents = graph.dfs("A")
        self.assertEqual(parents, {"A": None, "B": "A", "C": "A", "D": "B"})
        self.assertGreater(finishing_time["B"], discovery_time["B"])
        self.assertGreater(finishing_time["C"], discovery_time["C"])
        self.assertGreater(finishing_time["D"], discovery_time["D"])

    def test_dfs_disconnected_graph(self):
        graph = Graph(representation='list')
        graph.addEdge("A", "B")
        graph.addEdge("C", "D")
        discovery_time, finishing_time, parents = graph.dfs("A")
        self.assertEqual(discovery_time["A"], 1)
        self.assertEqual(finishing_time["A"], 4)
        self.assertEqual(parents["B"], "A")
        self.assertIsNone(parents["C"])
        self.assertEqual(parents["D"], "C")
        self.assertEqual(discovery_time["C"], 5)
        self.assertEqual(finishing_time["C"], 8)
        self.assertEqual(discovery_time["D"], 6)
        self.assertEqual(finishing_time["D"], 7)

    def test_dfs_directed_graph(self):
        graph = Graph(representation='list', is_directed=True)
        graph.addEdge("A", "B")
        graph.addEdge("B", "C")
        graph.addEdge("C", "D")
        discovery_time, finishing_time, parents = graph.dfs("A")
        self.assertEqual(parents, {"A": None, "B": "A", "C": "B", "D": "C"})
        self.assertGreater(finishing_time["B"], discovery_time["B"])
        self.assertGreater(finishing_time["C"], discovery_time["C"])
        self.assertGreater(finishing_time["D"], discovery_time["D"])

    def test_dfs_weighted_graph(self):
        graph = Graph(representation='list', is_weighted=True)
        graph.addEdge("A", "B", weight=5)
        graph.addEdge("B", "C", weight=3)
        graph.addEdge("C", "D", weight=2)
        discovery_time, finishing_time, parents = graph.dfs("A")
        self.assertEqual(parents, {"A": None, "B": "A", "C": "B", "D": "C"})
        self.assertGreater(finishing_time["B"], discovery_time["B"])
        self.assertGreater(finishing_time["C"], discovery_time["C"])
        self.assertGreater(finishing_time["D"], discovery_time["D"])

    def test_dfs_nonexistent_vertex(self):
        graph = Graph(representation='list')
        graph.addEdge("A", "B")
        with self.assertRaises(ValueError):
            graph.dfs("Z")


if __name__ == '__main__':
    unittest.main()
