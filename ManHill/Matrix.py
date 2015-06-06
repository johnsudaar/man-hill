# Man Hill project
# By Pierre Collet, Damien Teodori and Jonathan Hurter

# Edge.py

class Matrix(object):

	def __init__(self):
        self._edges = []

	def loadFromJson(self,json_data):
        for._edges = json.load(json_data)

	def toJson(self):

	def getNodeTo(self, node):
        node_to = []
        for edge in self._edges:
            if edge.isOut(node):
                note_to.append(edge.getIn())
        return node_to

	def getNodeFrom(self, node):
        node_from = []
        for edge in self._edges:
            if edge.isIn(node):
                node_from.append(edge.getOut())
        return node_from

	def set(self,in,out,pheromone,val_pos, val_neg):
        for edge in self._edges:
            if edge.isSame(in,out):
                edge.setValue(pheromone,val_pos,val_neg)
                return

        # Will only go to this line if the they is no edge found
        self._edges.append(Edge({'node_in':in,"node_out":out,"pheromones":{pheromone:[val_pos,val_neg]}}))
