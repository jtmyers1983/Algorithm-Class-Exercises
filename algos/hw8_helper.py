import graph

g1 = graph.random_graph(10,0.15,directed=False,seed=2018)
g2 = graph.random_graph(10,0.20,directed=False,seed=2018)
g3 = graph.random_graph(10,0.22,directed=False,seed=2018)

# Note for homework 8
# g1 is the graph shown in the image rg_10_15_2018.png
# g2 is the graph shown in the image rg_10_20_2018.png
# g3 is the graph shown in the image rg_10_22_2018.png

# check if (3,9) is an edge in g1.  It is!
e = (3,9)
if e in g1:
	print("Yes, the edge", e, "is in g1.")
else:
	print("No, the edge", e, "is not in g1." )

# check if (3,9) is an edge in g1.  It is not.
e = (3,0)
if e in g1:
	print("Yes, the edge", e, "is in g1.")
else:
	print("No, the edge", e, "is not in g1." )

# traverse the neighbors of a given node. May be needed for last problem.
for v in g1.Neighbors[8]:
	print(v, "is a neighbor of 8")

