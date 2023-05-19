from queue import PriorityQueue

class Graph_uniform:
    def __init__(self, directed=True):
        self.edges = {}
        self.directed = directed

    def add_edge(self, node1, node2, weight, __reversed=False):
        try:
            neighbors = self.edges[node1]
        except KeyError:
            neighbors = {}
        neighbors[node2] = weight
        self.edges[node1] = neighbors
        if not self.directed and not __reversed:
            self.add_edge(node2, node1, weight, True)

    def neighbors(self, node):
        try:
            return self.edges[node]
        except KeyError:
            return {}

    def uniform_cost_search(self, start, setOfGoals):
        found, fringe, visited, came_from, cost_so_far = False, PriorityQueue(), set([start]), {start: None}, {start: 0}
        fringe.put((0, start))
        print('{:11s} | {}'.format('Expand Node', 'Fringe'))
        print('--------------------')
        print('{:11s} | {}'.format('-', start))
        while not found and not fringe.empty():
            _, current = fringe.get()
            print('{:11s}'.format(current), end=' | ')
            if current in setOfGoals:
                found = True
                goal = current
                break
            for node, cost in self.neighbors(current).items():
                new_cost = cost_so_far[current] + cost
                if node not in cost_so_far or new_cost < cost_so_far[node]:
                    cost_so_far[node] = new_cost
                    visited.add(node)
                    fringe.put((new_cost, node))
                    came_from[node] = current
            print(', '.join([n for _, n in list(fringe.queue)]))
        if found:
            print()
            return came_from,cost_so_far[goal[0]], goal
        else:
            print('No path from {} to {}'.format(start, goal))

    @staticmethod
    def print_path(came_from, goal):
        parent = came_from[goal]
        if parent:
            Graph_uniform.print_path(came_from, parent)
        else:
            print(goal, end='')
            return
        print(' =>', goal, end='')

    def __str__(self):
        return str(self.edges)


G = Graph_uniform(directed = True)



