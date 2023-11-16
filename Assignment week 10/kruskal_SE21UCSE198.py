class Kruskal:
    def set_disjoint(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
        
    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)

        if root1 != root2:
            if self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1

    def kruskal(self,graph):
        vertices = set(graph.keys())
        edges = []

        for vertex in vertices:
            for neighbor, weight in graph[vertex]:
                edges.append((vertex, neighbor, weight))

        edges.sort(key=lambda x: x[2])

        mst_edges = []
        self.set_disjoint(vertices)

        for edge in edges:
            vertex1, vertex2, weight = edge
            if self.find(vertex1) != self.find(vertex2):
                mst_edges.append((vertex1, vertex2, weight))
                self.union(vertex1, vertex2)

        return mst_edges

graph = {
    'A': [("B",6),("D",6),("C",6)],
    'B': [("A",6),("C",1),("E",2)],
    'C': [("A",6),("B",1),("D",2),("E",7)],
    'D': [("A",6),("C",2),("J",18)],
    "E" : [("B",2),("C",7),("F",4)],
    "F" : [("E",4),("G",11),("H",10)],
    "G" : [("C",2),("F",11),("H",22),("I",2)],
    "H" : [("F",10),("G",22),("I",12),("K",25)],
    "I" : [("G",2),("H",12),("K",16),("J",1)],
    "J" : [("D",18),("I",1),("L",8)],
    "K" : [("I",16),("H",25),("L",3)],
    "L" : [("J",8),("K",3)]
}

tree = Kruskal()
min_spanning_tree = tree.kruskal(graph)
print("Minimum Spanning Tree:")
cost = 0
for edge in min_spanning_tree:
    cost+=edge[2]
    print(f"{edge[0]} - {edge[1]}")

print("Total cost ",cost)