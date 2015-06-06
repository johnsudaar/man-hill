# Man Hill project
# By Pierre Collet, Damien Teodori and Jonathan Hurter

# Matrix.py

from ManHill.Edge import Edge

class Matrix(object):

	def __init__(self,edges):
		self._edges = []
		for edge in edges:
			self._edges.append(Edge(edge))

	def getTable(self):
		table = []
		for edge in self._edges
			table.append(edge.getTable())

	def getEdgesTo(self, node):
		edges_to = []
		for edge in self._edges:
			if edge.isOut(node):
				edges_to.append(edge)
		return edges_to

	def getEdgesFrom(self, node):
		edges_from = []
		for edge in self._edges:
			if edge.isIn(node):
				edges_from.append(edge)
		return edges_from

	def getEdge(node_in,node_out):
		for edge in self._edges:
			if edge.isSame(node_in,node_out):
				return edge
		edge = Edge({'node_in':node_in,"node_out":node_out,"pheromones":{pheromone:[0,0]}})
		self._edges.append(edge)
		return edge

	def set_edge(self, edge, pheromone,val_pos, val_neg):
		self.set(edge.getIn(), edge.getOut(), pheromone, val_pos, val_neg)

	def set(self,node_in,node_out,pheromone,val_pos, val_neg):
		self.getEdge(node_in, node_out).setValue(pheromone,val_pos,val_neg)
