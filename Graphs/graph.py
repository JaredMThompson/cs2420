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

    def find_shortest_path(self, item):
        pass