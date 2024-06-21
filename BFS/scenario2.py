from collections import deque

class Node:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.neighbors = []

class Graph:
    def __init__(self):
        self.nodes = {} 

    def add_node(self, name, data):
        self.nodes[name] = Node(name, data)

    def add_edge(self, node1, node2, directed=False):
        if node1 not in self.nodes:
            self.add_node(node1)
        if node2 not in self.nodes:
            self.add_node(node2)

        self.nodes[node1].neighbors.append(self.nodes[node2])
        if not directed:
            self.nodes[node2].neighbors.append(self.nodes[node1])

    def bfs(self, start):
        frontier = deque()
        frontier.append(self.nodes[start])
        visited = set()

        while frontier:
            curr = frontier.popleft()
            visited.add(curr)
            print(f"visited {curr.name}")
            for neighbor in curr.neighbors:
                if neighbor not in visited and neighbor not in frontier:
                    frontier.append(neighbor)
        
    def dfs(self, start):
        visited = set() 
        stack = []
        time = 1
        stack.append(self.nodes[start])
        visited.add(self.nodes[start])
        print(f"discovered node {self.nodes[start].name} at {time}")
        while stack:
            curr = stack[len(stack)-1]
            neighbor = self.get_first_neighbor(curr, visited)
            time += 1
            if neighbor:
                visited.add(neighbor)
                print(f"discovered node {neighbor.name} at {time}")
                stack.append(neighbor)
            else:
                print(f"finished node {curr.name} at {time}")
                stack.pop()

    def get_first_neighbor(self, node, visited):
        for n in node.neighbors:
            if n not in visited:
                return n
        return None

# Example usage
graph = Graph()
graph.add_node('A', data={'color': 'red'})
graph.add_node('B', data={'color': 'blue'})
graph.add_node('C', data={'color': 'green'})
graph.add_node('D', data={'color': 'yellow'})
graph.add_node('E', data={'color': 'purple'})
graph.add_node('F', data={'color': 'orange'})

edges = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'F'),
        ('E', 'F')
        ]

for from_val, to_val in edges:
    graph.add_edge(from_val, to_val)

graph.bfs('A')
graph.dfs('A')
