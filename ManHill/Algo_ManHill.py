# Man Hill project
# By Pierre Collet, Damien Teodori and Jonathan Hurter

# Algo_ManHill.py

import math

class Algo_ManHill(object):

	def __init__(self,matrix,users):
		self._matrix=matrix
		self._users = users

	def erosion(self, node_out, pheromone, coeff):
		tab=self._matrix.getEdgesTo(node_out)
		for edge in tab:
			val_pos=edge.getPheromonePos(pheromone)*coeff
			val_neg=edge.getPheromoneNeg(pheromone)*coeff
			edge.setValue(pheromone,val_pos, val_neg)

	def retribution(self, user, success, pheromone, quantity=10, depth=3):
		total=quantity
		previous = Users.getPrevious(user)
		if len(previous) > depth:
			for j in range(0,depth): #nombre de rétributions
				var=math.floor(quantity/(j+2))
				
				if total < var: #permet de ne pas dépasser la quantité totale de phéromones à distribuer
					var = total

				total=total-var
				edge=self._matrix.getEdge(previous[j+1],previous[j])
				if success: #en cas de succes on modifie la phéromone positive
					tmp = edge.getPheromonePos() + var
					edge.setValue(pheromone,tmp, edge.getPheromoneNeg())
				else: #en cas d'échec on modifie la phéromone négative
					tmp = edge.getPheromoneNeg + var
					edge.setValue(pheromone,edge.getPheromonePos(),tmp)

	def getSuggestions(node_from, pheromone):
		final_tab = []
		tab=self._matrix.getEdgesfrom(node_from)
		for edge in tab:
			score = edge.getPheromonePos(pheromone) - edge.getPheromoneNeg(pheromone)
			final_tab.append({"edge":edge,"score":score})
		return final_tab

	def getUserPreferencesOnSuggestions(self, user,node_from, pheromone, start_forgetting = 20, forgetting_rate = 0.1):
		final_tab = []
		tab = self.getSuggestions(node_from, pheromone)
		for value in tab:
			position = self._users.getPositionOf(user, value["edge"].getNodeOut())
			if position == -1:
				final_tab.append(value)
			else:
				if position >start_forgetting:
					coeff=(start_forgetting-position)*forgetting_rate
				else:
					coeff=forgetting_rate
				if coeff >= 1:
					final_tab.append(value)
				else:
					final_tab.append({"edge":value["edge"] , "score": value["score"]*coeff}
		return final_tab
		
	def getFinalChoice(self, suggestions, number=3):
		suggested_score = [-1]*number
		suggested_nodes = [""]*number

		for value in tab:
			done = False
			for i in range(0,number)
				if !done:
					if value["score"] > suggested_score[i]:
						suggested_score[i]=value["score"]
						suggested_nodes[i]=value["edge"].getNodeOut()
						done = True
		return suggested_nodes

