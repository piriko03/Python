# DFS
def dfs(graph, start):
    visited = set()
    stack = [start]
    result = []

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            stack.extend(graph[vertex] - visited)

    return result


graph = {
    'A': {'B', 'C', 'D', 'E'},
    'B': {'A', 'F', 'G'},
    'C': {'A', 'K'},
    'D': {'A', 'M'},
    'E': {'A', 'L'},
    'F': {'B', 'H'},
    'G': {'B', 'I'},
    'H': {'F', 'J'},
    'I': {'G', 'J'},
    'J': {'H', 'I', 'Z'},
    'K': {'C', 'N', 'O'},
    'L': {'E', 'R'},
    'M': {'D', 'O'},
    'N': {'K', 'P'},
    'O': {'K', 'M', 'Q'},
    'P': {'N', 'Z'},
    'Q': {'O', 'Z'},
    'R': {'L', 'S', 'T'},
    'S': {'R'},
    'T': {'R'},
    'Z': {'J', 'P', 'Q'}
}

dfs_result = dfs(graph, 'A')
print("DFS Result:", dfs_result)


# BFS
def bfs(graph, start):
    visited = set()
    queue = [start]
    result = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(graph[vertex] - visited)

    return result


bfs_result = bfs(graph, 'A')
print("BFS Result:", bfs_result)
