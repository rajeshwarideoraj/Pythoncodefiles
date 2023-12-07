class Solution(object):
    def countPaths(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        def dfs(start, current, adjacency_list, visited, count):
            visited[current] = True

            # Check if the current node label is prime
            if is_prime(current):
                count[0] += 1

            # Explore neighbors
            for neighbor in adjacency_list[current]:
                if not visited[neighbor]:
                    dfs(start, neighbor, adjacency_list, visited, count)

            visited[current] = False  # Backtrack

        # Build an adjacency list representation of the tree
        adjacency_list = [[] for _ in range(n + 1)]
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])

        # Initialize the count of valid paths
        count = [0]

        # Start DFS from each node
        for i in range(1, n + 1):
            visited = [False] * (n + 1)
            dfs(i, i, adjacency_list, visited, count)

        # Return the total count of valid paths
        return count[0]
        