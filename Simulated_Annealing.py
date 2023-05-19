import random
import math

class SimulatedAnnealing:
    def __init__(self):
        self.edges = {}

    def add_edge(self, node1, node2, cost):
        try:
            neighbors = self.edges[node1]
        except KeyError:
            neighbors = {}
        neighbors[node2] = cost
        self.edges[node1] = neighbors

    def neighbors(self, node):
        try:
            return self.edges[node]
        except KeyError:
            return {}

    def simulated_annealing(self, start, goal, temperature, cooling_rate):
        current_node = start
        current_path = [current_node]

        while current_node != goal:
            neighbors = self.neighbors(current_node)

            if not neighbors:
                return None

            next_node = random.choice(list(neighbors.keys()))
            delta_cost = neighbors[next_node] - neighbors[current_node]

            if delta_cost < 0 or random.random() < math.exp(-delta_cost / temperature):
                current_node = next_node
                current_path.append(current_node)

            temperature *= cooling_rate

        return current_path

