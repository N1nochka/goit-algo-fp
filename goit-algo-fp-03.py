import networkx as nx
import heapq

def dijkstra_heap(graph, start):
    # Ініціалізуємо словник для збереження найкоротших відстаней
    shortest_distances = {node: float('inf') for node in graph.nodes()}
    shortest_distances[start] = 0
    
    # Ініціалізуємо бінарну купу та додаємо початкову вершину
    heap = [(0, start)]
    
    while heap:
        # Витягуємо вершину з мінімальною відстанню з бінарної купи
        current_distance, current_node = heapq.heappop(heap)
        
        # Переглядаємо всіх сусідів поточної вершини
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']
            
            # Оновлюємо відстань до сусіда, якщо знайдено коротший шлях
            if distance < shortest_distances[neighbor]:
                shortest_distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
    
    return shortest_distances

# Створюємо граф
G = nx.Graph()
G.add_edge('A', 'B', weight=5)
G.add_edge('A', 'C', weight=10)
G.add_edge('B', 'D', weight=3)
G.add_edge('C', 'D', weight=2)
G.add_edge('D', 'E', weight=4)

# Застосовуємо алгоритм Дейкстри з використанням бінарної купи
start_node = 'A'
shortest_distances = dijkstra_heap(G, start_node)

print("Найкоротші відстані від вершини", start_node, "до інших вершин:")
print(shortest_distances)