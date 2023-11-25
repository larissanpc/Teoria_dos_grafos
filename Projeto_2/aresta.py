'''
32139871 - Júlia Ronquetti Rodrigues
32195311 - Larissa Rafaela Rodrigues Nepomuceno
32137151 - Lívia Negrucci Cantowitz
32150032 - Rafael de Toledo Navarro

'''

class Aresta:
  def __init__(self,origem, destino, peso):
    self.vertice1 = origem
    self.vertice2 = destino
    self.peso = peso

class Vertice:
  def __init__(self, ponto, estacao):
    self.ponto = ponto
    self.estacao = estacao