import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())

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
        return graph

    def draw_tree(self, font_size=10):
        tree = nx.DiGraph()
        pos = {self.id: (0, 0)}
        tree = self.add_edges(tree, self, pos)
        labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}
        plt.figure(figsize=(8, 5))
        nx.draw(
            tree,
            pos=pos,
            labels=labels,
            arrows=False,
            node_size=2500,
        )
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
    root.draw_tree()

if __name__ == "__main__":
    main()