import networkx as nx 
import matplotlib.pyplot as plt 

class Node:
    def __init__(self, key):
        self.left = None 
        self.right = None 
        self.val = key 

# Функція для додавання ребер у граф відповідно до структури бінарного дерева.
def add_edges(graph, node, pos, x=0, y=0, layer=1, max_layer=1): 
    if node is not None:
        graph.add_node(node.val, label=node.val)  
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

# Функція для відображення бінарного дерева.
def draw_tree(tree_root): 
    tree = nx.DiGraph()  
    pos = {tree_root.val: (0, 0)}  
    tree.add_node(tree_root.val, label=tree_root.val)  
    add_edges(tree, tree_root, pos, max_layer=max_layer(tree_root))  
    labels = {node: node for node in tree.nodes()}  

    # Відображення графа за допомогою NetworkX та Matplotlib
    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, node_size=2000, with_labels=True, font_size=10)
    plt.show()

# Функція для знаходження максимальної глибини дерева
def max_layer(node):
    if node is None:
        return 0
    else:
        left_layer = max_layer(node.left)
        right_layer = max_layer(node.right)
        return max(left_layer, right_layer) + 1

# Приклад побудови бінарного дерева
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Відображення дерева
draw_tree(root)