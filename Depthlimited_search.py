# depth_limited.py

class Graph_depthlimited:
    def __init__(self, directed=True):
        self.edges = {}
        self.directed = directed

    def add_edge(self, node1, node2, __reversed=False):
        try:
            neighbors = self.edges[node1]
        except KeyError:
            neighbors = set()
        neighbors.add(node2)
        self.edges[node1] = neighbors
        if not self.directed and not __reversed:
            self.add_edge(node2, node1, True)

    def neighbors(self, node):
        try:
            return self.edges[node]
        except KeyError:
            return []

    def depth_limited_search(self, start, goal, depth_limit):
        return self.recursive_dls(start, goal, depth_limit)

    def recursive_dls(self, current, goal, depth_limit):
        if current == goal:
            return [current]
        elif depth_limit == 0:
            return []
        else:
            cutoff_occurred = False
            for node in self.neighbors(current):
                result = self.recursive_dls(node, goal, depth_limit - 1)
                if result == "cutoff":
                    cutoff_occurred = True
                elif result:
                    result.insert(0, current)
                    return result
            if cutoff_occurred:
                return "cutoff"
            else:
                return []

    def __str__(self):
        return str(self.edges)
