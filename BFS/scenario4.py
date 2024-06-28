from collections import deque

class Node:
    def __init__(self, value, data):
        self.value = value
        self.data = data
        self.neighbors = []

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, value, data=None):
        self.nodes[value] = Node(value, data)

    def add_edge(self, val1, val2, directed=True):
        if val1 not in self.nodes:
            self.add_node(val1)
        if val2 not in self.nodes:
            self.add_node(val2)

        self.nodes[val1].neighbors.append(self.nodes[val2])
        if not directed:
            self.nodes[val2].neighbors.append(self.nodes[val1])

    def bfs(self, start):
        if start not in self.nodes:
            return

        s_node = self.nodes[start]
        frontier = deque()
        found = set()

        frontier.append(s_node)
        found.add(s_node)
        print(f"found {s_node.value}")

        while frontier:
            curr = frontier.popleft() # Just do this. Was popping from end before
    
            for n in curr.neighbors:
                if n not in found:
                    found.add(n) # make sure to add to both
                    frontier.append(n)
                    print(f"found {n.value}")

            print(f"finished {curr.value}")
    
    def dfs(self, start, found=set()):
        if start not in self.nodes:
            return

        s_node = self.nodes[start]
        found.add(s_node)
        print(f"discovered {s_node.value}")

        for n in s_node.neighbors:
            if n not in found:
                self.dfs(n.value, found)

        print(f"finished {s_node.value}") # I was printing n.value instead of s_node.value

graph = Graph()
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')
graph.add_node('G')
graph.add_node('H')
graph.add_node('I')

graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'H')
graph.add_edge('C', 'I')
graph.add_edge('D', 'E')
graph.add_edge('D', 'F')
graph.add_edge('D', 'G')
graph.add_edge('E', 'H')
graph.add_edge('F', 'F')
graph.add_edge('G', 'H')
graph.add_edge('G', 'I')
graph.add_edge('H', 'A')
graph.add_edge('I', 'B')

graph.bfs('A')
graph.dfs('A')

