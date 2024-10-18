import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин
G.add_nodes_from(["Львів", "Самбір", "Дрогобич", "Стрий", "Борислав", "Трускавець"] )

# Додавання ребер (зв'язків між вершинами)
G.add_edges_from([("Львів", "Самбір"), ("Львів", "Дрогобич"), ("Львів", "Стрий"),
                  ("Самбір", "Дрогобич"), ("Самбір", "Борислав"),
                  ("Дрогобич", "Стрий"), ("Дрогобич", "Борислав"), ("Дрогобич", "Трускавець"),
                  ("Борислав", "Трускавець"), ("Трускавець", "Стрий")])

# Візуалізація графа
nx.draw(G, with_labels=True)
plt.show()

# Кількість вершин
num_nodes = G.number_of_nodes()

# Кількість ребер
num_edges = G.number_of_edges()

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")

#Використання вбудованих функцій networkX для DFS та BFS
dfs_path = list(nx.dfs_edges(G, source="Львів"))
bfs_path = list(nx.bfs_edges(G, source="Львів"))

print(f"DFS path: {dfs_path}")
print(f"BFS path: {bfs_path}")