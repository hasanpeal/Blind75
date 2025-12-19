from collections import defaultdict
from typing import List

def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Step 1: Handle edge cases
        # If there are no nodes, the graph is trivially a valid tree
        if not n:
            return True

        # If there are more edges than (n - 1), the graph cannot be a tree
        # A valid tree with n nodes must have exactly (n - 1) edges
        if len(edges) > (n - 1):
            return False

        # Step 2: Build the adjacency list to represent the graph
        # This is a defaultdict of lists where each node points to its neighbors
        adj = defaultdict(list)
        for a, b in edges:
            # Add both directions for an undirected graph
            adj[a].append(b)
            adj[b].append(a)

        # Step 3: Initialize a set to track visited nodes
        visited = set()

        # Step 4: Define a recursive DFS function to detect cycles and ensure connectivity
        def dfs(node, prevNode):
            # If the current node has already been visited, a cycle is detected
            if node in visited:
                return False
            
            # Mark the current node as visited
            visited.add(node)

            # Explore all the neighbors of the current node
            for nei in adj[node]:
                # Skip the neighbor that is the previous node (parent) in the DFS traversal
                if nei == prevNode:
                    continue

                # If the neighbor cannot be processed without a cycle, return False
                if not dfs(nei, node):
                    return False

            # If all neighbors are processed without detecting a cycle, return True
            return True

        # Step 5: Start DFS from node 0 and ensure the graph is connected and acyclic
        # The graph is valid if:
        # 1. DFS traversal from node 0 completes without detecting a cycle
        # 2. All nodes are visited (ensuring connectivity)
        return dfs(0, -1) and len(visited) == n