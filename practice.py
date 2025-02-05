from collections import defaultdict
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build the adjacency list to represent the graph
        # The graph is represented as a dictionary where each node maps to a list of its neighbors
        adj = defaultdict(list)
        for a, b in edges:
            # Add both directions for the undirected graph
            adj[a].append(b)
            adj[b].append(a)
        
        # Step 2: Initialize a set to keep track of visited nodes
        visited = set()

        # Step 3: Define a DFS function to traverse the graph
        def dfs(node):
            # Mark the current node as visited
            visited.add(node)
            # Traverse all unvisited neighbors of the current node
            for nei in adj[node]:
                if nei not in visited:
                    dfs(nei)
        
        # Step 4: Initialize a counter for the number of connected components
        count = 0
        
        # Step 5: Iterate through all nodes
        for i in range(n):
            # If a node is not visited, it's part of a new connected component
            if i not in visited:
                count += 1  # Increment the count for a new component
                # Perform DFS to mark all nodes in this component as visited
                dfs(i)
        
        # Step 6: Return the total number of connected components
        return count
