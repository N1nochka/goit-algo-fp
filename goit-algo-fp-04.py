import uuid
import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Node:
   def __init__(self, key, color="skyblue"):
       self.left = None
       self.right = None
       self.val = key
       self.color = color
       self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
   if node is not None:
       graph.add_node(node.id, color=node.color, label=node.val)
       if node.left:
           graph.add_edge(node.id, node.left.id)
           l = x - 1 / 2 ** layer
           pos[node.left.id] = (l, y - 1)
           l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
       if node.right:
           graph.add_edge(node.id, node.right.id)
           r = x + 1 / 2 ** layer
           pos[node.right.id] = (r, y - 1)
           r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
   return graph

def draw_tree(tree_root):
   tree = nx.DiGraph()
   pos = {tree_root.id: (0, 0)}
   tree = add_edges(tree, tree_root, pos)

   colors = [node[1]['color'] for node in tree.nodes(data=True)]
   labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

   plt.figure(figsize=(8, 5))
   nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
   plt.show()

def build_heap_tree(heap_array):
   root = Node(heap_array[0])
   heap = [root]

   for i in range(1, len(heap_array)):
       node = Node(heap_array[i])
       heap.append(node)
       parent_index = (i - 1) // 2
       if i % 2 == 0:
           heap[parent_index].right = node
       else:
           heap[parent_index].left = node

   return root

heap_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
heapq.heapify(heap_array)

heap_tree_root = build_heap_tree(heap_array)
draw_tree(heap_tree_root)
