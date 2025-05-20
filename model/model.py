import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.country = DAO.getDifferentCountry()
        self.anni = DAO.getAnni()
        self._grafo = nx.Graph()
        self.idMap = {}


    def getDifferentCountry(self):
        return self.country

    def buildGraph(self, country, anno):
        retailers = DAO.getNodes(country)
        for r in retailers:
            self.idMap[r.Retailer_code] = r
        # aggiungo i nodi
        self._grafo.add_nodes_from(retailers)
        # aggiungo archi
        self.addEdges(country, anno)
        print("grafo fatto")


    def addEdges(self, country, anno):
        edges = DAO.getArchi(country, anno, self.idMap)
        for e in edges:
            self._grafo.add_edge(e[0], e[1], weight=e[2])

    def getVolume(self):
        lista = {}
        for edge in self._grafo.edges:
            if edge[0].Retailer_code not in lista.keys():
                lista[edge[0].Retailer_code] = self._grafo[edge[0]][edge[1]]['weight']
            else:
                lista[edge[0].Retailer_code] += self._grafo[edge[0]][edge[1]]['weight']

            if edge[1].Retailer_code not in lista.keys():
                lista[edge[1].Retailer_code] = self._grafo[edge[0]][edge[1]]['weight']
            else:
                lista[edge[1].Retailer_code] += self._grafo[edge[0]][edge[1]]['weight']

        lista = sorted(lista.items(), key=lambda x: x[1], reverse=True)

        return lista[:5]

