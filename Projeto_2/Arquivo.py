'''
32139871 - Júlia Ronquetti Rodrigues
32195311 - Larissa Rafaela Rodrigues Nepomuceno
32137151 - Lívia Negrucci Cantowitz
32150032 - Rafael de Toledo Navarro
'''

from aresta import Aresta, Vertice
from grafoMatrizND import GrafoMatND

pontos = []
listaArestas = []

def leArquivoMatriz(): 
  with open("grafo.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    for i, linha in enumerate(linhas): # i: percorre linhas txt, line: conteúdo da linha
      if i == 0:
        tipo_grafo = linha
      elif i == 1:
        tamanho_inicial = int(linha)
        #grafo=GrafoMatND(tamanho_inicial)
      else:
        if i == tamanho_inicial+2:
          qtde_arestas = linha
        elif '"' in linha:
          linha_separa = linha.split('"')
          ponto_turi = linha_separa[1]
          estacao_metro = linha_separa[3]
          vertice = Vertice(ponto_turi, estacao_metro)
          pontos.append(vertice)
          #print(vertice)
              
        else: #Arestas
          arestas_separa = linha.split(", ")
          #print(arestas_separa)
          a_1 = arestas_separa[0]
          a_2 = arestas_separa[1]
          peso = arestas_separa[2]
          #print(f"a1:{a_1}, a2:{a_2}, peso: {peso}")
          arestaObj = Aresta(a_1, a_2, float(peso))         
            #grafo.insereA(a_1, a_2, int(peso))       
          listaArestas.append(arestaObj)
      
  grafo = GrafoMatND(len(pontos))
      # Inserindo vértices no grafo com a lista criada anteriormente
  #for tupla in pontos: 
    #ponto, estacao = tupla
  grafo.insereVerticeInicial(pontos)
    #print(nome_ponto)
      # Inserindo arestas no grafo  
  for aresta in listaArestas:
    grafo.insereA(aresta.vertice1, aresta.vertice2, aresta.peso)      
            #Fechando o arquivo txt
  arquivo.close()
  return grafo
