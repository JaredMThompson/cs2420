from graph import Graph
import csv

def main():
    with open("graph_input.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        vertices = int(next(reader)[0])
        graph = Graph(vertices)

        print("\n\nNeighbors:")
        edges = int(next(reader)[0])
        for i in range(edges):
            edge = next(reader)
            graph.add_edge(int(edge[0]), int(edge[1]))
        for i in range(len(graph.neighbors)):
            print(f'{i} = {graph.neighbors[i]}')

        print("\n\nTests:")
        tests = int(next(reader)[0])
        for i in range(tests):
            test = next(reader)
            path = graph.find_shortest_path(int(test[0]), int(test[1]))
            print(f'From {test[0]} to {test[1]}: {path}')
        


if __name__ == '__main__':
    main()