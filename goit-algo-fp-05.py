import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())
        self.color = None  

    def add_edges(self, graph, node, pos, x=0, y=0, layer=1):
        if node is not None:
            graph.add_node(node.id, label=node.val)
            if node.left:
                graph.add_edge(node.id, node.left.id)
                l = x - 1 / 2 ** layer
                pos[node.left.id] = (l, y - 1)
                l = self.add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
            if node.right:
                graph.add_edge(node.id, node.right.id)
                r = x + 1 / 2 ** layer
                pos[node.right.id] = (r, y - 1)
                r = self.add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
            self.color = None  
        return graph

    def dfs_traversal(self, visited=None):
        if visited is None:
            visited = set()
        visited.add(self)

        for neighbor in [self.left, self.right]:
            if neighbor and neighbor not in visited:
                neighbor.color = "#FF0000"  
                neighbor.dfs_traversal(visited)

    def bfs_traversal(self):
        queue = deque([self])

        while queue:
            current_node = queue.popleft()
            if current_node:
                current_node.color = "#00FF00"  
                for neighbor in [current_node.left, current_node.right]:
                    if neighbor:
                        queue.append(neighbor)
                        neighbor.color = "#00FF00"  

    def draw_tree(self, traversal_type, font_size=10):
        tree = nx.DiGraph()
        pos = {self.id: (0, 0)}
        tree = self.add_edges(tree, self, pos)

        colors = self.generate_colors(traversal_type)

        for node_id, node_data in tree.nodes(data=True):
            node_data["color"] = colors.pop(0) 

        labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}
        node_colors = [node[1]["color"] for node in tree.nodes(data=True)]
        nodelist = [node[0] for node in tree.nodes(data=True)]  

        plt.figure(figsize=(8, 5))
        nx.draw(
            tree,
            pos=pos,
            labels=labels,
            arrows=False,
            node_size=2500,
            node_color=node_colors,
            font_size=font_size,
            font_color="white",
            nodelist=nodelist  
        )
        plt.show()

    def generate_colors(self, traversal_type):
        if traversal_type == "DFS":
            base_color = (0.05, 0.588, 0.941)  
        elif traversal_type == "BFS":
            base_color = (0.8, 0, 0) 

        colors = []
        num_colors = 15
        for i in range(num_colors):
            intensity = 0.07 * i
            color = (
                max(0, base_color[0] - intensity),
                max(0, base_color[1] - intensity),
                max(0, base_color[2] - intensity),
            )
            colors.append(color)
        return colors[::-1]

def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)
    root.dfs_traversal()  
    root.draw_tree(traversal_type="DFS")  
    root.bfs_traversal()  
    root.draw_tree(traversal_type="BFS") 

if __name__ == "__main__":
    main()