from collections import deque

class Node:
    def __init__(self, value, data):
        self.value = value
        self.data = data
        self.distance = float('inf')
        self.neighbors = []

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value, data):
        self.nodes[value] = Node(value, data)

    def add_edge(self, from_val, to_val):
        if from_val not in self.nodes:
            self.add_node(from_val)
        if to_val not in self.nodes:
            self.add_node(to_val)

        self.nodes[from_val].neighbors.append(self.nodes[to_val])
        self.nodes[to_val].neighbors.append(self.nodes[from_val])

    def bfs(self, start):
        if start in self.nodes:
            start_node = self.nodes[start]
        frontier = deque()
        start_node.distance = 0
        frontier.appendleft(start_node)
        visited = set()

        while (frontier):
            curr = frontier.pop()
            if curr not in visited:
                visited.add(curr)
                if curr.distance == 2:
                    print(f"The node {curr.value} has data {curr.data} and is {curr.distance} away from the root")
                for neighbor in curr.neighbors:
                    neighbor.distance = curr.distance + 1
                    frontier.appendleft(neighbor)


    def dfs(self, start):
        visited = set()
        if start in self.nodes:
            start_node = self.nodes[start]
        stack = []
        time = 1
        stack.append(start_node)
        print(f"discovered node {start_node.value} at time {time}")
        while stack:
            curr = stack[len(stack) - 1]
            time += 1
            # get first unvisited neighbor and add to stack. if there are none, finish node
            child = self.get_first_child(curr, visited)
            visited.add(curr)
            if child:
                print(f"discovered node {child.value} at time {time}")
                stack.append(child)
            else:
                print(f"finished node {curr.value} at time {time}")
                stack.pop()

    def get_first_child(self, node, visited):
        for neighbor in node.neighbors:
            if neighbor not in visited:
                return neighbor
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
