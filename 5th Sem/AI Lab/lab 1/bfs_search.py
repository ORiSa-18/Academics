def bfs_search(graph,target):
    for node in graph:
        if node == target:
            return True
        else:
            for child in node:
                if child == target:
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
    if bfs_search(graph1, 'E'):
        print("Found")
    else:
        print("Not Found")

main()
