import heapq

print("\n\n----------------- PRIMS ALGORITHM -------------------------")
def prims(graph, start):
    visited = set()
    mst = []
    pq = [(0, start, None)]

    while pq:
        weight, node, parent = heapq.heappop(pq)
        if node in visited:
            continue
        
        visited.add(node)
        if parent is not None:
            mst.append((parent, node, weight))
        for neighbor, w in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (w, neighbor, node))
    return mst

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print("\n\n")
print("Graph :",graph)
print(prims(graph, 'A'))

print("\n\n----------------- #### -------------------------")
