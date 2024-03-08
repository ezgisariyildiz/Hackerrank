class QueueUsingTwoStacks:
    def __init__(self):
        self.stack_in = []  # Giriş için bir yığın
        self.stack_out = []  # Çıkış için bir yığın

    def enqueue(self, x):
        self.stack_in.append(x)  # Giriş yığınına eleman ekleme

    def dequeue(self):
        if not self.stack_out:
            # Çıkış yığını boşsa, giriş yığınından tüm elemanları çıkarıp çıkış yığınına taşı
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            # Eğer çıkış yığını boş değilse, en tepedeki elemanı çıkar
            return self.stack_out.pop()

    def front(self):
        if not self.stack_out:
            # Çıkış yığını boşsa, giriş yığınından tüm elemanları çıkarıp çıkış yığınına taşı
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if self.stack_out:
            # Eğer çıkış yığını boş değilse, en tepedeki elemanı döndür
            return self.stack_out[-1]

# Sorguları işle
def process_queries(queries):
    q = QueueUsingTwoStacks()
    results = []
    for query in queries:
        query_type = query[0]
        if query_type == 1:
            q.enqueue(query[1])
        elif query_type == 2:
            q.dequeue()
        elif query_type == 3:
            results.append(q.front())
    return results

if __name__ == '__main__':
    query_count = int(input())
    queries = []
    for _ in range(query_count):
        query = list(map(int, input().split()))
        queries.append(query)

    # Sorguları işle ve sonuçları yazdır
    results = process_queries(queries)
    for result in results:
        print(result)
