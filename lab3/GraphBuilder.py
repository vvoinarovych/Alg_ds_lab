class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, source, destination, weight=1):
        self.adjacency_matrix[source][destination] = weight

    def display_adjacency_matrix(self):
        print("Macierz sąsiedztwa:")
        for row in self.adjacency_matrix:
            print(row)

    def display_adjacency_list(self):
        print("Lista sąsiedztwa:")
        for vertex in range(self.num_vertices):
            neighbors = []
            for dest in range(self.num_vertices):
                weight = self.adjacency_matrix[vertex][dest]
                if weight != 0:
                    neighbors.append((dest, weight))
            print(f"Wierzchołek {vertex}: {neighbors}")

    def display_graph(self):
        print("Interpretacja graficzna:")
        for source in range(self.num_vertices):
            for dest in range(self.num_vertices):
                weight = self.adjacency_matrix[source][dest]
                if weight != 0:
                    print(f"{source} --({weight})--> {dest}")

    def create_graph(self):
        graph_type = input("Podaj typ grafu\n1-skierowany\n2-nieskierowany\n3-ważony\n4-inny\n: ")
        for source in range(self.num_vertices):
            for dest in range(self.num_vertices):
                if graph_type == "3":
                    weight = int(input(f"Podaj wagę krawędzi {source} -> {dest}: "))
                else:
                    weight = 1
                self.add_edge(source, dest, weight)


def main():
    num_vertices = int(input("Podaj liczbę wierzchołków: "))
    graph = Graph(num_vertices)
    graph.create_graph()
    print()
    graph.display_adjacency_matrix()
    print()
    graph.display_adjacency_list()
    print()
    graph.display_graph()


if __name__ == "__main__":
    main()
