from graph import UndirectedGraph, DirectedGraph

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