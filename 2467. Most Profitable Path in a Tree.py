class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """
        from collections import defaultdict

        # Build adjacency list representation of the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # Find Bob's path from his starting position to the root (node 0)
        bob_path = {}

        def find_bob_path(node, parent, depth):
            if node == 0:
                bob_path[node] = depth
                return True
            for neighbor in tree[node]:
                if neighbor != parent and find_bob_path(neighbor, node, depth + 1):
                    bob_path[node] = depth
                    return True
            return False

        find_bob_path(bob, -1, 0)

        # DFS to find Alice's optimal path
        max_profit = [float('-inf')]  # Use list to allow modification inside dfs

        def dfs(node, parent, depth, current_profit):
            # Calculate income at current node
            if node in bob_path:
                if depth < bob_path[node]:  # Alice reaches first
                    current_profit += amount[node]
                elif depth == bob_path[node]:  # Both reach simultaneously
                    current_profit += amount[node] // 2
                # Otherwise, Bob already took the amount, do nothing
            else:
                current_profit += amount[node]

            # If at a leaf node, update max profit
            if len(tree[node]) == 1 and node != 0:
                max_profit[0] = max(max_profit[0], current_profit)
                return

            # Explore children
            for neighbor in tree[node]:
                if neighbor != parent:
                    dfs(neighbor, node, depth + 1, current_profit)

        dfs(0, -1, 0, 0)
        return max_profit[0]
