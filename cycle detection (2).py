class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def is_cycle(self):
        visited = set()
        path = set()

        def dfs(node):
            visited.add(node)
            path.add(node)

            for neighbour in self.graph.get(node, []):
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
                elif neighbour in path:
                    return True

            path.remove(node)
            return False

        for node in self.graph:
            if node not in visited:
                if dfs(node):
                    return True

        return False


# Create graph
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 1)

# Check cycle
if g.is_cycle():
    print("Cycle detected")
else:
    print("No cycle")