import networkx as nx
import random
import time
import matplotlib.pyplot as plt

vertex_counts = [100,200,500,700,1000,2000,3000,4000,5000]  # список количества вершин
time_records = []

for vertex_count in vertex_counts:
    # Генерируем список ребер
    edge_list = [(i, j) for i in range(vertex_count) for j in range(i + 1, vertex_count)]
    random.shuffle(edge_list)

    # Создаем граф
    G = nx.Graph()
    G.add_edges_from(edge_list)

    # Показываем пользователю список ребер
    print(f"List of edges for graph with {vertex_count} vertices:")
    print(', '.join(map(str, edge_list)))

    # Просим пользователя выбрать ребро для удаления и проверяем его ввод
    while True:
        edge_to_remove = input("Please enter the edge to remove in the format 'a b': ")
        edge_to_remove = tuple(map(int, edge_to_remove.split()))

        if edge_to_remove in edge_list:
            break
        else:
            print("The entered edge does not exist. Please try again.")

    # Удаляем выбранное ребро и замеряем время
    start_time = time.time()
    G.remove_edge(*edge_to_remove)
    end_time = time.time()
    edge_removal_time = end_time - start_time

    # Выполняем сортировку вершин по убыванию степени и замеряем время
    start_time = time.time()
    sorted_vertices = sorted(G.nodes(), key=lambda x: G.degree(x), reverse=True)
    end_time = time.time()
    sorting_time = end_time - start_time
    total_time = edge_removal_time + sorting_time

    # Добавляем общее время выполнения в список
    time_records.append(total_time)

    print(f"Sorted vertices for modified graph: {sorted_vertices}\n")
    print(f"Total running time of the algorithm : {format(total_time,'.10f')} seconds")

# Построим график времени выполнения в зависимости от количества вершин
plt.plot(vertex_counts, time_records)
plt.xlabel('Number of vertices')
plt.ylabel('Execution time (s)')
plt.title('Execution time vs Number of vertices')
plt.show()
