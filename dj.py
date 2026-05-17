import heapq


def dj(n,src,adj):
    dist = [float('inf')]*n
    dist[src] = 0

    pq = [(0,src)]

    while pq:
        d , node = heapq.heappop(pq)

        for neigh , wt in adj[node]:
            if d + wt < dist[neigh]:
                dist[neigh] = wt +d
                heapq.heappush(pq,(wt+d , neigh))

    return dist



n = int(input("Enter Number of vertices :"))
e = int(input("Enter Number of Edges :"))

adj =[[]]*n
print("Enter Edges like u v w :\n")

for _ in range(e):
    u,v,w = map(int,input().split())
    adj[u].append((v,w))

result = dj(n,0,adj)

print("DISTANCE FROM SRC to ALL Nodes :")
for i in range(n):
    print(f"{0} - >{i} == {result[i]}")



    



      
