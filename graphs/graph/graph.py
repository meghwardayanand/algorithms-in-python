
class Graph:
    def __init__(self, representation='list'):
        if representation not in ['list', 'matrix']:
            raise ValueError("Representation must be either 'list' or 'matrix'")

        self.representation = representation
        self.graph = {}     # For adjacency list representation
        self.matrix = []    # For adjacency matrix representation
        self.vertices = []  # List to hold vertices for matrix index mapping

    def add_vertex(self, vertex):
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

    def add_edge(self, vertex1, vertex2):
        if self.representation == 'list':
            if vertex1 not in self.graph:
                self.add_vertex(vertex1)

            if vertex2 not in self.graph:
                self.add_vertex(vertex2)

            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

        elif self.representation == 'matrix':
            if vertex1 not in self.vertices:
                self.add_vertex(vertex1)

            if vertex2 not in self.vertices:
                self.add_vertex(vertex2)

            index1 = self.vertices.index(vertex1)
            index2 = self.vertices.index(vertex2)
            self.matrix[index1][index2] = 1
            self.matrix[index2][index1] = 1

    def remove_vertex(self, vertex):
        if self.representation == 'list':
            if vertex in self.graph:
                for neighbor in self.graph[vertex]:
                    self.graph[neighbor].remove(vertex)

                del self.graph[vertex]

        elif self.representation == 'matrix':
            if vertex in self.vertices:
                index = self.vertices.index(vertex)
                self.vertices.remove(vertex)
                self.matrix.pop(index)

                for row in self.matrix:
                    row.pop(index)

    def remove_edge(self, vertex1, vertex2):
        if self.representation == 'list':
            if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)

            if vertex2 in self.graph and vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

        elif self.representation == 'matrix':
            if vertex1 in self.vertices and vertex2 in self.vertices:
                index1 = self.vertices.index(vertex1)
                index2 = self.vertices.index(vertex2)
                self.matrix[index1][index2] = 0
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
