def dfs_search(graph, node, visited, target):
    if target == node:
        return True
    if node not in visited:
        visited.append(node)
        for child in graph[node]:
            if dfs_search(graph, child, visited, target): 
                return True
    return False

def main():
    graph1 = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    visited = []
    if dfs_search(graph1, 'A', visited, 'F'):
        print("Found")
    else:
        print("Not Found")

main()
