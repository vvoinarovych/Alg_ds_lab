def DFS(graph, s):
    visited = set()
    stack = [s]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            neighbors = graph[vertex]
            stack.extend(neighbors)
