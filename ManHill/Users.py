# Man Hill project
# By Pierre Collet, Damien Teodori and Jonathan Hurter

# User.py

class Users(object):

    def __init__(self,table):
        self._table = table

    def getTable(self):
        return self._table

    def getElo(self, user):
        if self._table.has_key(user):
            return self._table[user]["elo"]
        else:
            return 0
    def setElo(self, user, elo):
        if self._table.has_key(user):
            self._table[user]["elo"] = elo
        else:
            self._table[user] = {"elo": elo, "previous":[]}

    def getPrevious(self,user):
        if self._table.has_key(user):
            self._table[user]["previous"]
        else:
            return []

    def getPositionOf(self,user,node):
        for i in range(0,len(self._table[user]["previous"]))
            if self._table[user]["previous"][i] == node
                return i
        return -1

    def addPrevious(self,user,node,max_nodes=50):
        if self._table.has_key(user):
            self._table[user]["previous"].insert(0,node)
        else:
            self._table[user]["previous"] = [node]
        self._table[user]["previous"] = self._table[user]["previous"][:max_nodes]
