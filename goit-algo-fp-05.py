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
        visited = set()

        while queue:
            current_node = queue.popleft()
            if current_node and current_node not in visited:
                current_node.color = "#00FF00"  
                visited.add(current_node)
                for neighbor in [current_node.left, current_node.right]:
                    if neighbor:
                        queue.append(neighbor)
                        neighbor.color = "#00FF00"  

def dfs_visualize(root, total_steps=1):
    visited, stack = set(), [(root, 0)]
    colors = {}
    step = 0
    while stack:
        node, depth = stack.pop()
        if node not in visited:
            visited.add(node)
            colors[node.id] = generate_color(step, total_steps)
            step += 1
            if node.right:
                stack.append((node.right, depth + 1))
            if node.left:
                stack.append((node.left, depth + 1))
    return colors


def bfs_visualize(root, total_steps=1):
    visited, queue = set(), [root]
    colors = {}
    step = 0
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            colors[node.id] = generate_color(step, total_steps)
            step += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return colors

def generate_color(step, total_steps):
    base_color = [135, 206, 250]  # світло-блакитний (skyblue) у форматі RGB
    darken_factor = step / (2 * total_steps)  # Наскільки темнішим має бути кожен наступний вузол
    new_color = [int(c * (1 - darken_factor)) for c in base_color]
    return f'#{new_color[0]:02x}{new_color[1]:02x}{new_color[2]:02x}'

def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = tree_root.add_edges(tree, tree_root, pos)
    node_colors = [colors.get(node, 'skyblue') for node in tree.nodes()]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

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
    
    colors_bfs = bfs_visualize(root, total_steps=15)
    draw_tree(root, colors_bfs)

    colors_dfs = dfs_visualize(root, total_steps=15)
    draw_tree(root, colors_dfs)

if __name__ == "__main__":
    main()