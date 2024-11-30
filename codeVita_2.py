from collections import deque

def solve_desert_queen():
    # Read input
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(input().split())
    
    # Find start and end positions
    start, end = None, None
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)
    
    # Possible movement directions
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    # Initialize distance and visited tracking
    dist = [[float('inf')] * N for _ in range(N)]
    dist[start[0]][start[1]] = 0
    
    # Queue for BFS
    queue = deque([start])
    
    # BFS to find minimum water consumption path
    while queue:
        x, y = queue.popleft()
        
        # If reached end, return water consumption
        if (x, y) == end:
            return dist[x][y]
        
        # Try all four directions
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            # Check grid boundaries and mountain cells
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] != 'M':
                # Calculate water cost
                water_cost = 0
                if grid[x][y] != 'T' or grid[nx][ny] != 'T':
                    water_cost = 1
                
                # Update if new path is cheaper
                new_dist = dist[x][y] + water_cost
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    queue.append((nx, ny))
    
    # If no path found
    return -1

# Run the solution
print(solve_desert_queen())