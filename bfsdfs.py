from collections import deque

def bfs(nv , adj, start):
    visited = [False] * nv
    queue = deque()
    queue.append(start)
    visited[start] = True

    print("BFS Traversal:", end=" ")
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for neigh in adj[node]:
            if not visited[neigh]:
                visited[neigh] = True
                queue.append(neigh)
    print()

def dfs(adj, start):
    visited = [False] * len(adj)
    stack = [start]

    print("DFS Traversal:", end=" ")
    while stack:
        node = stack.pop()
        if not visited[node]:
            print(node, end=" ")
            visited[node] = True
            # push neighbors
            for neigh in adj[node]:
                if not visited[neigh]:
                    stack.append(neigh)
    print()


# --- Main Program ---
n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

adj = [[]]*n

print("Enter edges (u v):")
for _ in range(e):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)   # undirected graph

while True:
    print("\nMenu:")
    print("1. BFS")
    print("2. DFS")
    print("3. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        start = int(input("Enter starting node: "))
        bfs(n,adj, start)
    elif choice == 2:
        start = int(input("Enter starting node: "))
        dfs(adj, start)
    elif choice == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
