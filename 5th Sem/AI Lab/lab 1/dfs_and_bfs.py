
def bfs(graph):
    que=[]
    for i in graph:
        que.append(i)
        break
    for root in que:
        for element in graph[root]:
            if element not in que:
                que.append(element)
        print(root)

def dfs(graph):
    stack =[]
    visited = []
    for i in graph:
        stack.append(i)
        break
    while stack:
        current = stack.pop()
        visited.append(current)
        for element in graph[current]:
            if element not in stack:
                stack.append(element)
    for i in visited[::-1]:
        print(i)



def main():
    graph1 = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    dfs(graph1)


main()
