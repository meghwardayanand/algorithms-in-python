
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
