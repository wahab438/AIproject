from collections import deque

class Graph_bidirectional:
    def __init__(self, directed=True):
        self.edges_forward = {}
        self.edges_backward = {}
        self.directed = directed

    def add_edge(self, node1, node2, __reversed=False):
        try:
            neighbors = self.edges_forward[node1]
        except KeyError:
            neighbors = set()
        neighbors.add(node2)
        self.edges_forward[node1] = neighbors
        if not self.directed and not __reversed:
            self.add_edge(node2, node1, True)

        try:
            neighbors = self.edges_backward[node2]
        except KeyError:
            neighbors = set()
        neighbors.add(node1)
        self.edges_backward[node2] = neighbors
        if not self.directed and not __reversed:
            self.add_edge(node1, node2, True)

    def neighbors_forward(self, node):
        try:
            return self.edges_forward[node]
        except KeyError:
            return []

    def neighbors_backward(self, node):
        try:
            return self.edges_backward[node]
        except KeyError:
            return []

    def bidirectional_search(self, start, goals):
        found, fringe_forward, fringe_backward, visited_forward, visited_backward, came_from_forward, came_from_backward = False, deque([start]), deque([goals[0]]), set([start]), set([goals[0]]), {start: None}, {goals[0]: None}
        print('{:11s} | {:11s} | {}'.format('Expand Node', 'Forward Fringe', 'Backward Fringe'))
        print('------------------------------------------------------------')
        print('{:11s} | {:11s} | {}'.format('-', start, goals[0]))
        while not found and len(fringe_forward) and len(fringe_backward):
            current_forward = fringe_forward.pop()
            print('{:11s}'.format(current_forward), end=' | ')
            if current_forward in visited_backward:
                found = True
                intersection_node = current_forward
                break
            for node_forward in self.neighbors_forward(current_forward):
                if node_forward not in visited_forward:
                    visited_forward.add(node_forward)
                    fringe_forward.appendleft(node_forward)
                    came_from_forward[node_forward] = current_forward

            current_backward = fringe_backward.pop()
            print('{:11s}'.format(current_backward), end=' | ')
            if current_backward in visited_forward:
                found = True
                intersection_node = current_backward
                break
            for node_backward in self.neighbors_backward(current_backward):
                if node_backward not in visited_backward:
                    visited_backward.add(node_backward)
                    fringe_backward.appendleft(node_backward)
                    came_from_backward[node_backward] = current_backward

            print(', '.join(fringe_forward), end=' | ')
            print(', '.join(fringe_backward))

        if found:
            path_forward = self.reconstruct_path(came_from_forward, intersection_node)
            path_backward = self.reconstruct_path(came_from_backward, intersection_node)
            path_backward.reverse()
            path = path_forward + path_backward[1:]
            return path, intersection_node
        else:
            return None, None

    @staticmethod
    def reconstruct_path(came_from, goal):
        path = []
        current = goal
        while current is not None:
            path.append(current)
            current = came_from[current]
        path.reverse()
        return path

    @staticmethod
    def print_path(path, goal):
        print(' -> '.join(path), end='')
        print(' ->', goal)
