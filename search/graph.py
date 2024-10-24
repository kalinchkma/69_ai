

class Graph:
   def __init__(self, size):
      self.adj_matrix = [[0] * size for _ in range(size)]
      self.size = size
      self.vertex_data = [''] * size

   def add_vertex(self, vertex, data):
      if 0 <= vertex < self.size:
         self.vertex_data[vertex] = data
   
   def add_edge(self, u, v):
      if 0 <= u < self.size and 0 <= v < self.size:
         self.adj_matrix[u][v] = 1
         self.adj_matrix[v][u] = 1
   
   def print_graph(self):
      print("Adjacency matrix:")
      for row in self.adj_matrix:
         print(' '.join(map(str, row)))
      print("\nVertex Data:")
      for vertex, data in enumerate(self.vertex_data):
         print(f"Vertex {vertex}: {data}")
      


if __name__ == "__main__":
   g = Graph(7)

   g.add_vertex(0, 'A')
   g.add_vertex(1, 'B')
   g.add_vertex(2, 'C')
   g.add_vertex(3, 'D')
   g.add_vertex(4, 'E')
   g.add_vertex(5, 'F')
   g.add_vertex(6, 'G')

   g.add_edge(0, 1)
   g.add_edge(1, 2)
   g.add_edge(1, 6)
   g.add_edge(1, 4)
   g.add_edge(2, 5)
   g.add_edge(2, 6)
   g.add_edge(3, 4)
   g.add_edge(3, 5)

   g.print_graph()

   t = [1, 2, 3, 4, 5]
   print(t[:-1])


   
   


