'''
32139871 - Júlia Ronquetti Rodrigues
32195311 - Larissa Rafaela Rodrigues Nepomuceno
32137151 - Lívia Negrucci Cantowitz
32150032 - Rafael de Toledo Navarro

'''

import os

class GrafoMatND:
  TAM_MAX_DEFAULT = 100  # qtde de vértices máxima default
  inf = float('inf')
  
  # construtor da classe grafo
  def __init__(self, n=TAM_MAX_DEFAULT, rotulado = False):
    self.n = n  # número de vértices
    self.m = 0  # número de arestas
    self.rotulado = rotulado
    self.grafo = [[self.inf for i in range(n)] for j in range(n)]
    self.vertices=[]
    
# Insere uma aresta no Grafo tal que
# v é grafoacente a w
  def insereVerticeInicial(self, vertice):
    #print(self.vertices)
    self.vertices = vertice
    
  def insereVertice(self, vertice):
    self.vertices.append(vertice)
    self.n += 1
    #atualiza a matriz de adjacência pra incluir o novo vértice
    nova_linha = [self.inf] * self.n
    for linha in self.grafo:
      linha.append(self.inf)
    self.grafo.append(nova_linha)
    print("\nO ponto turistico e a estação foram inseridos")
    #for i in self.vertices:
      #print(i.ponto)
    
  def indiceNome(self, ponto):
    for i in range(len(self.vertices)):
      if self.vertices[i].ponto == ponto:
        return i
    return -1
        
  def insereA(self, v, w, rotulo = inf):
    posicao_v = self.indiceNome(v)
    posicao_w = self.indiceNome(w)
    if posicao_v != -1 and posicao_w != -1:
      if self.grafo[posicao_v][posicao_w] == self.inf:
        self.grafo[posicao_v][posicao_w] = rotulo
        self.grafo[posicao_w][posicao_v] = rotulo
        self.m+=1
      else:
        self.grafo[posicao_v][posicao_w] = rotulo
        self.grafo[posicao_w][posicao_v] = rotulo
    else:
      print("\n>>>Um dos pontos inseridos é inexistente")

  #Exercício 10
  def removerVertice(self, vertice):
    contem = False
    for i in self.vertices:
      if vertice in i.ponto:
        contem = True
    if contem:
      verticeIndex = self.indiceNome(vertice)
      # Removendo as arestas com todos os outros vértices primeiro antes de apagar as posições do vetor
      for i in range(self.n):
        vertice_dest = self.vertices[i].ponto # variável que pega todos os nomes dos vértices existentes na lista de nomes
        self.removeA(vertice,vertice_dest)# remove as ligações existentes com os outros vértices        
      # Atualiza a matriz (removendo os elementos)
      self.grafo.pop(verticeIndex) # Apaga o vértice 
      self.n -= 1 # Atualiza a quantidade de vértices  
      #Atualizando as colunas desalocando o espaço do antigo vértice
      for i in self.grafo:        
        i.pop(verticeIndex)
      self.vertices.pop(verticeIndex)
      #print(self.vertices)
    else:
      print("Ponto não está na lista")

  # remove uma aresta v->w do Grafo
  def removeA(self, v, w):
    posicao_v = self.indiceNome(v)
    posicao_w = self.indiceNome(w)
    if posicao_v != -1 and posicao_w != -1:
      # testa se temos a aresta
      if self.grafo[posicao_v][posicao_w] != self.inf and self.grafo[posicao_w][posicao_v] != self.inf:
        self.grafo[posicao_v][posicao_w] = self.inf
        self.grafo[posicao_w][posicao_v] = self.inf
        self.m -= 1
      # atualiza qtd arestas
    else:
      print("\n>>>Um dos pontos inseridos é inexistente")

  
  def conexo(self):
    visitado = [False] * self.n
    self.dfs(0, visitado)

    if all(visitado):
      return 1
    else: 
      return 0

  def dfs(self, v, visitado):
    visitado[v] = True
    for i in range(self.n):
      if self.grafo[v][i] != self.inf and not visitado[i]:
        self.dfs(i, visitado)

  def gravarDados(self):
    os.remove("grafo.txt")
    with open("grafo.txt", "w") as arquivo:
      for i in range(len(self.vertices)+2):
        if i == 0:
          arquivo.write("2\n")
        elif i == 1:
          arquivo.write(f"{self.n}\n")
        else:
          arquivo.write(f'"{self.vertices[i-2].ponto}" "{self.vertices[i-2].estacao}"\n')
      arquivo.write(f"{self.m}\n")
      aux = [linha[:] for linha in self.grafo]
      for i in range(self.n):
        for j in range(self.n):
          if aux[i][j] != self.inf:
            peso = self.grafo[i][j]
            arquivo.write(f"{self.vertices[i].ponto}, {self.vertices[j].ponto}, {peso}\n")
            aux[j][i]=self.inf
      arquivo.close()
          
        
  
  
  def show(self):
    print(f"\n n: {self.n:2d} ", end="")
    print(f"m: {self.m:2d}\n")
    for i in range(self.n):
      #print(f"Ponto turístico: '{self.vertices[i]}': ")
      for j in range(self.n):
        if self.grafo[i][j] != self.inf:
          print(f"{self.vertices[i].ponto}  ---> {self.vertices[j].ponto} || DISTANCIA = {self.grafo[i][j]}km")
      print("\n")