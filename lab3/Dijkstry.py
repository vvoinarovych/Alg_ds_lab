def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    queue = [(start, 0)]

    while queue:
        vertex, cost = queue.pop(0)

        for neighbor in graph[vertex]:
            new_cost = cost + graph[vertex][neighbor]

            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                queue.append((neighbor, new_cost))
        queue.sort(key=lambda x: x[1])

    return distances

#demo
graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 2},
    'D': {'B': 3, 'C': 2, 'E': 4},
    'E': {'D': 4}
}

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

print("Najkrótsze odległości z wierzchołka", start_vertex)
for vertex in distances:
    print("Do wierzchołka", vertex, ":", distances[vertex])
