from enum import Enum

from basic.queue.queue import Queue


class Color(Enum):
    WHITE = "white"
    GRAY = "gray"
    BLACK = "black"


class Graph:
    def __init__(self, representation='list', is_directed=False, is_weighted=False):
        if representation not in ['list', 'matrix']:
            raise ValueError("Representation must be either 'list' or 'matrix'")

        self.representation = representation
        self.is_directed = is_directed
        self.is_weighted = is_weighted
        self.graph = {}     # For adjacency list representation
        self.matrix = []    # For adjacency matrix representation
        self.vertices = []  # List to hold vertices for matrix index mapping

    def addVertex(self, vertex):
        if self.representation == 'list':
            if vertex not in self.graph:
                self.graph[vertex] = []

        elif self.representation == 'matrix':
            if vertex not in self.vertices:
                self.vertices.append(vertex)
                size = len(self.vertices)

                for row in self.matrix:
                    row.append(0)

                self.matrix.append([0] * size)

    def addEdge(self, vertex1, vertex2, weight=None):
        if self.representation == 'list':
            if vertex1 not in self.graph:
                self.addVertex(vertex1)

            if vertex2 not in self.graph:
                self.addVertex(vertex2)

            one_way_edge = (vertex2, weight) if self.is_weighted else vertex2
            two_way_edge = (vertex1, weight) if self.is_weighted else vertex1
            self.graph[vertex1].append(one_way_edge)
            if not self.is_directed:
                self.graph[vertex2].append(two_way_edge)

        elif self.representation == 'matrix':
            if vertex1 not in self.vertices:
                self.addVertex(vertex1)

            if vertex2 not in self.vertices:
                self.addVertex(vertex2)

            index1 = self.vertices.index(vertex1)
            index2 = self.vertices.index(vertex2)
            self.matrix[index1][index2] = weight if self.is_weighted else 1
            if not self.is_directed:
                self.matrix[index2][index1] = weight if self.is_weighted else 1

    def removeVertex(self, vertex):
        if self.representation == 'list':
            if vertex not in self.graph:
                return

            if not self.is_directed:
                for neighborhood in self.graph[vertex]:
                    neighbor, weight = neighborhood if self.is_weighted else (neighborhood, None)
                    connection = (vertex, weight) if self.is_weighted else vertex
                    self.graph[neighbor].remove(connection)

            del self.graph[vertex]

        elif self.representation == 'matrix':
            if vertex in self.vertices:
                index = self.vertices.index(vertex)
                self.vertices.remove(vertex)
                self.matrix.pop(index)

                for row in self.matrix:
                    row.pop(index)

    def _getEdge(self, from_vertex, to_vertex):
        for neighborhood in self.graph[from_vertex]:
            (neighbor, weight) = neighborhood if self.is_weighted else (neighborhood, None)
            if neighbor != to_vertex:
                continue

            return (neighbor, weight) if self.is_weighted else neighbor

    def removeEdge(self, vertex1, vertex2):
        if self.representation == 'list':
            if vertex1 in self.graph:
                edge = self._getEdge(vertex1, vertex2)
                if not edge:
                    return

                self.graph[vertex1].remove(edge)

            if self.is_directed:
                return

            if vertex2 in self.graph:
                edge = self._getEdge(vertex2, vertex1)
                if not edge:
                    return

                self.graph[vertex2].remove(edge)

        elif self.representation == 'matrix':
            if vertex1 in self.vertices and vertex2 in self.vertices:
                index1 = self.vertices.index(vertex1)
                index2 = self.vertices.index(vertex2)
                self.matrix[index1][index2] = 0
                if not self.is_directed:
                    self.matrix[index2][index1] = 0

    def display(self):
        print(self.__repr__())

    def bfs(self, start_vertex):
        if self.representation == 'list' and start_vertex not in self.graph:
            raise ValueError(f"Vertex {start_vertex} not found.")
        elif self.representation == 'matrix' and start_vertex not in self.vertices:
            raise ValueError(f"Vertex {start_vertex} not found.")

        vertices = self.graph.keys() if self.representation == "list" else self.vertices
        queue_size = len(vertices)
        colors = {vertex: Color.WHITE for vertex in vertices if vertex != start_vertex}
        distances = {vertex: float("inf") for vertex in vertices if vertex != start_vertex}
        parents = {vertex: None for vertex in vertices if vertex != start_vertex}
        queue = Queue(size=queue_size)

        queue.enqueue(start_vertex)
        parents[start_vertex] = None
        distances[start_vertex] = 0
        colors[start_vertex] = Color.GRAY

        while not queue.isEmpty():
            current_vertex = queue.dequeue()

            if self.representation == 'list':
                neighbors = self.graph[current_vertex]
                for neighbor in neighbors:
                    neighbor_vertex, weight =  neighbor if self.is_weighted else (neighbor, 1)
                    if colors[neighbor_vertex] == Color.WHITE:
                        colors[neighbor_vertex] = Color.GRAY
                        distances[neighbor_vertex] = distances[current_vertex] + weight
                        parents[neighbor_vertex] = current_vertex
                        queue.enqueue(neighbor_vertex)

                colors[current_vertex] = Color.BLACK

            elif self.representation == 'matrix':
                index = self.vertices.index(current_vertex)
                for neighbor_vertex_index, weight in enumerate(self.matrix[index]):
                    neighbor_vertex = self.vertices[neighbor_vertex_index]
                    if weight != 0 and colors[neighbor_vertex] == Color.WHITE:
                        colors[neighbor_vertex] = Color.GRAY
                        distances[neighbor_vertex] = distances[current_vertex] + weight
                        parents[neighbor_vertex] = current_vertex
                        queue.enqueue(neighbor_vertex)

                colors[current_vertex] = Color.BLACK

        return distances, parents

    def _dfs_visit(self, vertex, colors, discovery_time, finishing_time, parents, time):
        colors[vertex] = Color.GRAY
        time[0] += 1
        discovery_time[vertex] = time[0]

        if self.representation == 'list':
            neighbors = self.graph[vertex]
            for neighbor in neighbors:
                neighbor_vertex = neighbor[0] if self.is_weighted else neighbor
                if colors[neighbor_vertex] == Color.WHITE:
                    parents[neighbor_vertex] = vertex
                    self._dfs_visit(neighbor_vertex, colors, discovery_time, finishing_time, parents, time)

        elif self.representation == 'matrix':
            index = self.vertices.index(vertex)
            for neighbor_vertex_index, weight in enumerate(self.matrix[index]):
                neighbor_vertex = self.vertices[neighbor_vertex_index]
                if weight != 0 and colors[neighbor_vertex] == Color.WHITE:
                    parents[neighbor_vertex] = vertex
                    self._dfs_visit(neighbor_vertex, colors, discovery_time, finishing_time, parents, time)

        colors[vertex] = Color.BLACK
        time[0] += 1
        finishing_time[vertex] = time[0]

    def dfs(self, start_vertex):
        if self.representation == 'list' and start_vertex not in self.graph:
            raise ValueError(f"Vertex {start_vertex} not found.")
        elif self.representation == 'matrix' and start_vertex not in self.vertices:
            raise ValueError(f"Vertex {start_vertex} not found.")

        vertices = self.graph.keys() if self.representation == "list" else self.vertices
        colors = {vertex: Color.WHITE for vertex in vertices}
        discovery_time = {vertex: float("inf") for vertex in vertices}
        finishing_time = {vertex: float("inf") for vertex in vertices}
        parents = {vertex: None for vertex in vertices}
        time = [0]

        for vertex in vertices:
            if colors[vertex] == Color.WHITE:
                self._dfs_visit(vertex, colors, discovery_time, finishing_time, parents, time)

        return discovery_time, finishing_time, parents

    def __repr__(self):
        output = ""
        if self.representation == 'list':
            for vertex in self.graph:
                output += f"{vertex}: {self.graph[vertex]}\n"

        elif self.representation == 'matrix':
            output += "Adjacency Matrix:\n"
            output += "  " + " ".join(self.vertices) + "\n"
            for i, row in enumerate(self.matrix):
                output += f"{self.vertices[i]} " + " ".join(map(str, row)) + "\n"

        return output
