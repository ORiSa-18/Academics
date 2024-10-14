def dfs(graph,node,visited=set()):
    if node not in visited:
        visited.add(node)
        print(node,end=" ")
        for neighbor in graph[node]:
            dfs(graph,neighbor,visited)


def bfs(graph,start):
    que=deque([start])
    visited=set()
    visited.add(start)
    while que:
        node = que.popleft()
        print(node,end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                que.append(neighbor)
                visited.add(neighbor)


def ucs(graph,start,goal):
    que=[(0,start)]
    visited=set()
    while que:
        cost,node=heapq.heappop(que)
        if node==goal:
            return cost
        if node not in visited:
            visited.add(node)
            for neighbour,n_cost in graph[node]:
                if neighbour not in visited:
                    heapq.heappush(que,(n_cost+cost,neighbour))

def a_star(graph,start,goal,h):
    que=[(0,start)]
    visited=set()
    g_costs={start:0}
    came_from={start:None}
    while que:
        _,node = heapq.heappop(que)
        if node == goal:
            path=[]
            while node is not None:
                path.append(node)
                node = came_from[node]
            return g_costs[goal],path
        if node not in visited:
            visited.add(node)
            for neighbour,cost in graph[node]:
                new_cost = cost + g_costs[node]
                if neighbour not in visited or g_costs[neighbour]>new_cost:
                    g_costs[neighbour]=new_cost
                    f_cost=new_cost+h(neighbour)
                    heapq.heappush(que,(f_cost,neighbour))
                    came_from[neighbour]=node

def hill_climbing(start,neighbors,cost_fn):
    current=start
    while True:
        next_move=None
        for neighbor in neighbors(current):
            if cost_fn(neighbor)>cost_fn(current):
                next_move=neighbor
        if next_move==None:
            return current
        current=next_move
