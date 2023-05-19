
from collections import deque

class Graph_dfs:
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
        if not self.directed and not __reversed: self.add_edge(node2, node1, True)

    def neighbors(self, node):
        try:
            return self.edges[node]
        except KeyError:
            return []

    def depth_first_search(self, start, setOfGoal):
        found, fringe, visited, came_from = False, deque([start]), set([start]), {start: None}
        while not found and len(fringe):
            current = fringe.pop()
            if current in setOfGoal:
                found = True
                goal = current;
                break
            for node in self.neighbors(current):
                if node not in visited: visited.add(node); fringe.append(node); came_from[node] = current
        if found:
            print(); return came_from, current
        else:
            print('No path from {} to {}'.format(start, goal))

    @staticmethod
    def print_path(came_from, goal):
        parent = came_from[goal]
        if parent:
            Graph_dfs.print_path(came_from, parent)
        else:
            print(goal, end='');return
        print(' =>', goal, end='')

    def __str__(self):
        return str(self.edges)