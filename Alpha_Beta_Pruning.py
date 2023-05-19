class AlphaBetaPruning:
    def __init__(self):
        self.edges = {}

    def add_edge(self, node1, node2, value):
        try:
            neighbors = self.edges[node1]
        except KeyError:
            neighbors = {}
        neighbors[node2] = value
        self.edges[node1] = neighbors

    def neighbors(self, node):
        try:
            return self.edges[node]
        except KeyError:
            return {}

    def alpha_beta_search(self, start, depth, alpha, beta, maximizing_player):
        if depth == 0:
            return self.heuristic(start)

        if maximizing_player:
            value = float('-inf')
            for neighbor in self.neighbors(start):
                value = max(value, self.alpha_beta_search(neighbor, depth - 1, alpha, beta, False))
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value
        else:
            value = float('inf')
            for neighbor in self.neighbors(start):
                value = min(value, self.alpha_beta_search(neighbor, depth - 1, alpha, beta, True))
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return value

    def heuristic(self, node):
        # TODO: Implement your heuristic function here
        pass
