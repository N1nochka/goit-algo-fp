import networkx as nx
import matplotlib.pyplot as plt
import uuid
import matplotlib.colors as mcolors

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def add_edges(graph, node, pos, x=0, y=0, layer=1, max_layer=1):
    if node is not None:
        color = mcolors.to_hex(plt.cm.viridis(layer / max_layer))  # Генерація колірного коду
        if node.val == 1:  
            color = "#00008B"
        graph.add_node(node.val, color=color, label=node.val)
        if node.left:
            graph.add_edge(node.val, node.left.val)
            l = x - 1 / 2 ** layer
            pos[node.left.val] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1, max_layer=max_layer)
        if node.right:
            graph.add_edge(node.val, node.right.val)
            r = x + 1 / 2 ** layer
            pos[node.right.val] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1, max_layer=max_layer)

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.val: (0, 0)}
    add_edges(tree, tree_root, pos, max_layer=max_depth(tree_root))
    
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, node_color=colors, node_size=2000, with_labels=True, font_size=10)
    plt.show()

def dfs(node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node.val)
    print(node.val)
    if node.left and node.left.val not in visited:
        dfs(node.left, visited)
    if node.right and node.right.val not in visited:
        dfs(node.right, visited)

def bfs(node):
    visited = set()
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        visited.add(current_node.val)
        print(current_node.val)
        if current_node.left and current_node.left.val not in visited:
            queue.append(current_node.left)
        if current_node.right and current_node.right.val not in visited:
            queue.append(current_node.right)

def max_depth(node):
    if node is None:
        return 0
    else:
        left_depth = max_depth(node.left)
        right_depth = max_depth(node.right)
        return max(left_depth, right_depth) + 1

# Приклад використання
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Відображення дерева
draw_tree(root)
