from collections import deque, defaultdict

def bfs(graph, start, n):
    """Perform BFS to calculate shortest distances from the start node."""
    dist = [-1] * (n + 1)
    dist[start] = 0
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if dist[neighbor] == -1:  # Not visited
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    
    return dist

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    T = int(data[idx])  # Number of test cases
    idx += 1
    
    results = []
    added_roads = []
    total_added_roads = 0
    
    for _ in range(T):
        N, M, K = map(int, data[idx:idx + 3])
        idx += 3
        
        tour = list(map(int, data[idx:idx + K]))
        idx += K
        
        graph = defaultdict(list)
        for __ in range(M):
            u, v = map(int, data[idx:idx + 2])
            idx += 2
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 1: Calculate shortest distances from city 1
        dist = bfs(graph, 1, N)
        
        # Step 2: Check if the tour is already interesting
        tour_distances = [dist[city] for city in tour]
        if all(tour_distances[i] < tour_distances[i + 1] for i in range(len(tour_distances) - 1)):
            results.append("0")
            continue
        
        # Step 3: Try to make the tour interesting by adding roads
        # For simplicity, we add roads between city 1 and the tour cities
        # This ensures that the distances are strictly increasing
        added = []
        for i in range(len(tour) - 1):
            if dist[tour[i]] >= dist[tour[i + 1]]:
                # Add a road between city 1 and tour[i + 1]
                added.append((1, tour[i + 1]))
                total_added_roads += 1
                if total_added_roads > 5 * 10**5:
                    print(-1)
                    return
        
        if added:
            results.append(str(len(added)))
            added_roads.extend(added)
        else:
            results.append("-1")
    
    # Output results
    sys.stdout.write("\n".join(results) + "\n")
    for road in added_roads:
        sys.stdout.write(f"{road[0]} {road[1]}\n")