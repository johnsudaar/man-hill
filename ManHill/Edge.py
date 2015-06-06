# Man Hill project
# By Pierre Collet, Damien Teodori and Jonathan Hurter

# Edge.py

class Edge(object):

	def __init__(self,tab):
		self._table=tab

	def setValue(self, pheromone, pos, neg):
		if _table["pheromones"].has_key(pheromone):
			_table["pheromones"][pheromone][0]=pos
			_table["pheromones"][pheromone][1]=neg
		else:
			_table["pheromones"].update({pheromone: [pos,neg]})

	def getAllPheromones(self):
		return _table["pheromones"]

	def isIn(self, value):
		return self.getNodeIn()==value

	def isOut(self, value):
		return self.getNodeOut()==value
			
	def isSame(self, node_i, node_o):
		if (self.getNodeOut()==node_o) and (self.getNodeIn()== node_i):
			return True
		else:
			return False

	def getNodeIn(self):
		return _table["node_in"]

	def getNodeOut(self):
		return _table["node_out"]