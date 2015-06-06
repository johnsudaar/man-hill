import json

from ManHill.Algo_ManHill import Algo_ManHill
from ManHill.Matrix import Matrix
from ManHill.Users import Users
from ManHill.Nodes import Nodes

class ManHill(object):

    def __init__(self, json_data='{"matrix":[],"users":[],"nodes":[]}'):
        tables = json.load(json_data)
        self._matrix = Matrix(tables["matrix"])
        self._users = Users(tables["users"])
        self._nodes = Nodes(tables["nodes"])
        self._algo_mh = Algo_ManHill(self._matrix, self._users);

    def getJson(self):
        tables={}
        tables["matrix"] = self._matrix.getTable()
        tables["users"] = self._users.getTable()
        tables["nodes"] = self._nodes.getTable()

        return json.dump(tables)

    def tick(user,current_node, pheromone, success, user,coeff=0.9, depth=3,quantity=10,max_nodes=50):
        self._users.addPrevious(user,current_node,max_nodes)
        self._algo_mh.erosion(current_node, pheromone, coeff)
        self._algo_mh.retribution(user,success,pheromone,quantity,depth)

    def getSuggestions(current_node,user):
        return self._algo_mh.
