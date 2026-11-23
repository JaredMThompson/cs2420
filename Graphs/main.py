from graph import Graph
import csv

def main():
    with open("graph_input.csv", mode="r", newline="") as file:
        reader = csv.reader(file)
        current = 0
        edges = 0
        for row in reader:
            current += 1
            if current == 1:
                graph = Graph(int(row[0]))
            elif current == 2:
                edges = int(row[0])
            else:
                


if __name__ == '__main__':
    main()