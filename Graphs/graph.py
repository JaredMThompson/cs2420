class Graph():
    
    def __init__(self, num_verts):
        self.neighbors = []
        for i in range(num_verts):
            self.neighbors.append([])

    def add_edge(self, v1, v2):
        self.neighbors[v1].append(v2)

    def is_edge(self, v1, v2):
        if self.neighbors[v1][v2]:
            return True
        return False

    def get_neighbors(self, v):
        return self.neighbors[v]

    def find_shortest_path(self, v1, v2):
        if v1 == v2:
            return [v1]
        queue = [[v1]]
        while len(queue):
            current = queue.pop()
            current_neighbors = self.neighbors[current[-1]]
            if v2 in current_neighbors:
                current.append(v2)
                return current
            for item in current_neighbors:
                if item not in current:
                    queue.insert(0, current + [item])