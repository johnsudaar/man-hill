# Man Hill project
# By Pierre Collet, Damien Teodori and Jonathan Hurter

# Matrix.py

import json
from Edge import Edge

class Matrix(object):

	def __init__(self):
		self._edges = []

	def loadFromJson(self,json_data):
		all_edges = json.load(json_data)
		for edge in all_edges:
			self._edges.append(Edge(edge))

	def toJson(self):
		return

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

	def set_edge(self, edge, pheromone,val_pos, val_neg):
		self.set(edge.getIn(), edge.getOut(), pheromone, val_pos, val_neg)

	def set(self,node_in,node_out,pheromone,val_pos, val_neg):
		for edge in self._edges:
			if edge.isSame(node_in,node_out):
				edge.setValue(pheromone,val_pos,val_neg)
				return

		# Will only go to this line if the they is no edge found
		self._edges.append(Edge({'node_in':node_in,"node_out":node_out,"pheromones":{pheromone:[val_pos,val_neg]}}))
