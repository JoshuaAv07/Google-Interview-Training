from graph import UndirectedGraph, DirectedGraph, WeightedGraph

ug = UndirectedGraph()
print("Undirected Graph: ")
ug.add_edge("A", "B")
ug.add_edge("A", "C")
ug.add_edge("B", "D")
ug.add_edge("C", "D")
ug.display()

dg = DirectedGraph()
print("\nDirected Graph: ")
dg.add_edge("A", "B")
dg.add_edge("A", "C")
dg.add_edge("B", "D")
dg.add_edge("C", "D")
dg.display()

wg = WeightedGraph()
print("\nWeighted Directed Graph: ")
wg.add_edge("A", "B", 5)
wg.add_edge("A", "C", 2)
wg.add_edge("B", "D", 1)
wg.add_edge("C", "D", 7)
wg.add_edge("C", "B", 3)
wg.display()

print("\nShortest distances from A using Dijkstra:")
distances = wg.dijkstra("A")
for vertex, dist in distances.items():
    print(f"{vertex}: {dist}")