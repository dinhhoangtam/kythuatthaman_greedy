import matplotlib.pyplot as plt
import networkx as nx

class Edge:
    def __init__(self, length, start, end):
        self.length = length
        self.start = start
        self.end = end

def read_file(file_name):
    edge_list = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            n = int(file.readline().strip())
            for i in range(n):
                line = file.readline().strip().split()
                for j in range(i + 1, n):
                    item = line[j]
                    try:
                        length = float(item)
                    except ValueError:
                        length = item  # Giữ nguyên dưới dạng chuỗi
                    edge_list.append(Edge(length, i, j))
        print("Đọc dữ liệu từ file thành công!")
    except FileNotFoundError:
        print("Mở file gặp lỗi!")
        exit(1)
    return edge_list, n

def bubble_sort(edge_list):
    n = len(edge_list)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if isinstance(edge_list[j].length, float) and isinstance(edge_list[j - 1].length, float):
                if edge_list[j].length < edge_list[j - 1].length:
                    edge_list[j], edge_list[j - 1] = edge_list[j - 1], edge_list[j]

def has_degree_three(PA, new_edge):
    start_count = sum(1 for edge in PA if edge.start == new_edge.start or edge.end == new_edge.start)
    end_count = sum(1 for edge in PA if edge.start == new_edge.end or  edge.end == new_edge.end)
    return start_count == 2 or end_count == 2

def initialize_forest(n):
    return list(range(n))

def find_root(parent, u):
    while u != parent[u]:
        u = parent[u]
    return u

def forms_cycle(root_start, root_end):
    return root_start == root_end

def update_forest(parent, root1, root2):
    parent[root2] = root1

def greedy_algorithm(edge_list, n):
    parent = initialize_forest(n)
    PA = []
    for edge in edge_list:
        if not isinstance(edge.length, float):
            continue  # Bỏ qua các cạnh có độ dài không phải số thực
        root_start = find_root(parent, edge.start)
        root_end = find_root(parent, edge.end)
        if not has_degree_three(PA, edge) and not forms_cycle(root_start, root_end):
            PA.append(edge)
            update_forest(parent, root_start, root_end)
    return PA

def find_hamiltonian_cycle(edge_list, n):
    graph = nx.Graph()
    for edge in edge_list:
        if isinstance(edge.length, float):
            graph.add_edge(edge.start, edge.end, weight=edge.length)

    def backtrack(path):
        if len(path) == n:
            if graph.has_edge(path[-1], path[0]):
                return path + [path[0]]
            else:
                return None
        for neighbor in graph.neighbors(path[-1]):
            if neighbor not in path:
                new_path = backtrack(path + [neighbor])
                if new_path:
                    return new_path
        return None

    for start in range(n):
        cycle = backtrack([start])
        if cycle:
            return cycle
    return None

def draw_graph(edge_list, pos, title, ax, node_color='skyblue', edge_color='skyblue'):
    G = nx.Graph()
    for edge in edge_list:
        if isinstance(edge.length, float):
            G.add_edge(chr(65 + edge.start), chr(65 + edge.end), weight=edge.length)

    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_color=node_color, node_size=1500, font_size=15, ax=ax, edge_color=edge_color)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, label_pos=0.3, ax=ax)
    ax.set_title(title)

def calculate_total_length(edge_list):
    return sum(edge.length for edge in edge_list if isinstance(edge.length, float))

def calculate_hamiltonian_cycle_length(cycle, graph):
    total_length = 0
    for i in range(len(cycle) - 1):
        total_length += graph[cycle[i]][cycle[i + 1]]['weight']
    return total_length

def format_hamiltonian_cycle(cycle, graph):
    formatted_edges = []
    for i in range(len(cycle) - 1):
        start, end = cycle[i], cycle[i + 1]
        weight = graph[start][end]['weight']
        formatted_edges.append((i + 1, chr(65 + start), chr(65 + end), weight))
    # Sắp xếp các cạnh theo độ dài tăng dần
    formatted_edges.sort(key=lambda x: x[3])
    return formatted_edges

def main():
    edge_list, n = read_file("D://Ghi_Dia_Do_An/Do_An_2.txt")

    # Sao lưu danh sách ban đầu
    original_edge_list = list(edge_list)

    bubble_sort(edge_list)  # Sắp xếp danh sách
    sorted_edge_list = list(edge_list)  # Sao lưu danh sách sau khi sắp xếp

    graph = nx.Graph()
    for edge in edge_list:
        if isinstance(edge.length, float):
            graph.add_edge(edge.start, edge.end, weight=edge.length)

    hamiltonian_cycle = find_hamiltonian_cycle(edge_list, n)
    if hamiltonian_cycle:
        print("Cây khung nhỏ nhất:", ' -> '.join(chr(65 + node) for node in hamiltonian_cycle))
        hamiltonian_cycle_length = calculate_hamiltonian_cycle_length(hamiltonian_cycle, graph)
        print(f"Tổng độ dài các cạnh cây khung nhỏ nhất: {hamiltonian_cycle_length:.2f}")
        formatted_hamiltonian_cycle = format_hamiltonian_cycle(hamiltonian_cycle, graph)

        fig, ax = plt.subplots(3, 2, figsize=(16, 16))

        pos = nx.spring_layout(
            nx.Graph(
                [(chr(65 + edge.start), chr(65 + edge.end), {'weight': edge.length})
                 for edge in edge_list if isinstance(edge.length, float)]
            ),
            k=0.6,
            seed=42
        )

        H = nx.Graph()
        for i in range(len(hamiltonian_cycle) - 1):
            H.add_edge(chr(65 + hamiltonian_cycle[i]), chr(65 + hamiltonian_cycle[i + 1]), weight=graph[hamiltonian_cycle[i]][hamiltonian_cycle[i + 1]]['weight'])

        # Đồ thị ban đầu
        draw_graph(original_edge_list, pos, "Đồ thị với trọng số các cạnh (Ban đầu)", ax[0, 0])
        ax[0, 0].set_title("Đồ thị với trọng số các cạnh (Ban đầu)",fontsize=18)
        # Chu trình Hamilton
        edge_labels = nx.get_edge_attributes(H, 'weight')
        nx.draw(H, pos, with_labels=True, node_color='lightgreen', node_size=1500, font_size=15, ax=ax[0, 1], edge_color='green')
        nx.draw_networkx_edge_labels(H, pos, edge_labels=edge_labels, font_size=10, label_pos=0.3, ax=ax[0, 1])
        ax[0, 1].set_title("Đồ thị cây khung nhỏ nhất",fontsize=18)

        # Danh sách các cạnh ban đầu
        original_edges_text = "\n".join(
            ["{:<5} {:<5} {:<5} {:<5}".format(idx + 1, chr(65 + edge.start), chr(65 + edge.end), edge.length)
             for idx, edge in enumerate(original_edge_list)]
        )
        ax[1, 0].text(0.1, 0.5, original_edges_text, fontsize=10, verticalalignment='center', horizontalalignment='left')
        ax[1, 0].set_title("Danh sách các cạnh (Ban đầu)",fontsize=18)
        ax[1, 0].axis('off')

        # Danh sách các cạnh sau khi sắp xếp
        sorted_edges_text = "\n".join(
            ["{:<5} {:<5} {:<5} {:<10}".format(idx + 1, chr(65 + edge.start), chr(65 + edge.end), edge.length)
             for idx, edge in enumerate(sorted_edge_list)]
        )
        ax[1, 1].text(0.1, 0.5, sorted_edges_text, fontsize=10, verticalalignment='center', horizontalalignment='left')
        ax[1, 1].set_title("Danh sách các cạnh (Sau khi sắp xếp)",fontsize=18)
        ax[1, 1].axis('off')

        # Chu trình Hamilton và tổng độ dài
        hamiltonian_text = "\n".join(
            ["{:<5} {:<5} {:<5} {:<5.2f}".format(edge[0], edge[1], edge[2], edge[3]) for edge in formatted_hamiltonian_cycle]
        )
        hamiltonian_text += f"\n\nTổng độ của các cạnh các cạnh cây khung nhỏ nhất : {hamiltonian_cycle_length:.2f}"
        ax[2, 0].text(0.1, 0.5, hamiltonian_text, fontsize=15, verticalalignment='center', horizontalalignment='left')
        ax[2, 0].set_title("Danh Sách Cây Khung Nhỏ Nhất",fontsize=18)
        ax[2, 0].axis('off')

        # Tắt ô trống ở góc dưới bên phải
        ax[2, 1].axis('off')

        fig.suptitle("CHƯƠNG TRÌNH ĐƯỜNG ĐI NGƯỜI GIAO HÀNG KỸ THUẬT THAM ĂN", fontsize=25, fontweight='bold')
        plt.tight_layout(rect=[0, 0, 1, 0.95])  # Chỉnh layout để không tràn tiêu đề
        plt.show()
    else:
        print("Không tìm thấy chu trình Hamilton.")

if __name__ == "__main__":
    main()
