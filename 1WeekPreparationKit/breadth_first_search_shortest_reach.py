# ************ DAY6: MOCK TESTS: Breadth-First Search: Shortest Reach ************************

from collections import deque
import os

def bfs(n, m, edges, s):
    # Graph oluştur
    graph = {i: [] for i in range(1, n + 1)}
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)
    
    # Başlangıç düğümünden diğer düğümlere olan en kısa mesafeyi hesapla
    distances = [-1] * (n + 1)  # Başlangıç düğümü hariç tüm düğümlerin mesafesi -1 olarak başlatılır
    distances[s] = 0  # Başlangıç düğümüne olan mesafe 0 olarak ayarlanır
    queue = deque([s])  # BFS için kullanılacak kuyruk oluşturulur

    while queue:
        node = queue.popleft()  # Kuyruktan bir düğüm alınır
        for neighbor in graph[node]:  # Düğümün komşuları üzerinde gezin
            if distances[neighbor] == -1:  # Eğer komşu daha önce ziyaret edilmemişse
                distances[neighbor] = distances[node] + 6  # Mesafesi güncellenir
                queue.append(neighbor)  # Komşu kuyruğa eklenir
    
    # Sonuç dizisini oluştur ve başlangıç düğümünü hariç tutarak döndür
    return [distances[i] for i in range(1, n + 1) if i != s]

# Test etmek için
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
