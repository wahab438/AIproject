from queue import PriorityQueue

class Graph_bestfirst:
    def __init__(self, directed=True):
        self.edges = {}
        self.heuristics = {}
        self.directed = directed

    def add_edge(self, node1, node2, cost=1, __reversed=False):
        try:
            neighbors = self.edges[node1]
        except KeyError:
            neighbors = {}
        neighbors[node2] = cost
        self.edges[node1] = neighbors
        if not self.directed and not __reversed:
            self.add_edge(node2, node1, cost, True)

    def set_heuristics(self, heuristics={}):
        self.heuristics = heuristics

    def neighbors(self, node):
        try:
            return self.edges[node]
        except KeyError:
            return []

    def cost(self, node1, node2):
        try:
            return self.edges[node1][node2]
        except:
            return float('inf')

    def best_first_search(self, start, set_of_goals):
        found, fringe, visited, came_from = False, PriorityQueue(), set([start]), {start: None}
        goal = None
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))
        fringe.put((self.heuristics[start], start))
        while not found and not fringe.empty():
            _, current = fringe.get()
            print('{:11s}'.format(current), end=' | ')
            if current in set_of_goals:
                found = True
                goal = current
                break
            for node in self.neighbors(current):
                if node not in visited:
                    visited.add(node)
                    came_from[node] = current
                    fringe.put((self.heuristics[node], node))
            print(', '.join([str(item[1]) for item in fringe.queue]))
        if found:
            print()
            return came_from, goal
        else:
            print('No path from {} to {}'.format(start, goal))
            return None, None

    @staticmethod
    def print_path(came_from, goal):
        parent = came_from[goal]
        if parent:
            Graph_bestfirst.print_path(came_from, parent)
        else:
            print(goal, end='')
            return
        print(' =>', goal, end='')

    def __str__(self):
        return str(self.edges)

