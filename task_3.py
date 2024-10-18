import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Створення вагового графа
G = nx.Graph()
G.add_edge("Львів", "Самбір", weight=74)
G.add_edge("Львів", "Дрогобич", weight=78)
G.add_edge("Львів", "Стрий", weight=71)
G.add_edge("Самбір", "Дрогобич", weight=33)
G.add_edge("Самбір", "Борислав", weight=37)
G.add_edge("Дрогобич", "Борислав", weight=12)
G.add_edge("Дрогобич", "Стрий", weight=29)
G.add_edge("Дрогобич", "Трускавець", weight=12)
G.add_edge("Борислав", "Трускавець", weight=10)
G.add_edge("Трускавець", "Стрий", weight=36)


# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    pq = [(0, start)]

    while pq:
        print("\nСтан черги пріоритетів (pq): ", pq)
        print("Поточний стан найкоротших шляхів (sp):", shortest_paths)

        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    # Повертаємо та виводимо найкоротші шляхи
    print(f"\nНайкоротші шляхи від '{start}':")
    for vertex, distance in shortest_paths.items():
        print(f"Відстань до {vertex}: {distance} км")

    return shortest_paths


# Використання алгоритму Дейкстри
shortest_paths = dijkstra(G, "Львів")

# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()
