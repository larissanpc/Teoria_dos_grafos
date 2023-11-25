'''
32139871 - Júlia Ronquetti Rodrigues
32195311 - Larissa Rafaela Rodrigues Nepomuceno
32137151 - Lívia Negrucci Cantowitz
32150032 - Rafael de Toledo Navarro

Nesse código, nós implementamos um grafo onde os vertices são pontos turisticos e as arestas 
que ligam os vertices são os caminhos entre eles pelas estações de metro. Cada aresta possui 
um peso, que é a distancia entre uma estação e outra.
'''

import Arquivo
from aresta import Aresta
from aresta import Vertice
from grafoMatrizND import GrafoMatND

importGrafo = True


def menu(opcao):
  global grafo, importGrafo
  if opcao == 1:  #Leitura do arquivo
    if importGrafo == True:
      grafo = Arquivo.leArquivoMatriz()
      importGrafo = False
    else:
      print("O arquivo txt já foi inserido no grafo.")

  elif opcao == 2:  #Grava grafo atual no arquivo
    if importGrafo == False:
      grafo.gravarDados()
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 3:
    if importGrafo == False:
      nome_ponto = input(
          "Insira um nome para o ponto turistico que você deseja inserir: "
      ).upper()
      nome_estacao = input(
          "Insira um nome para a estacao que você deseja inserir: ").upper()
      vertice = Vertice(nome_ponto, nome_estacao)
      grafo.insereVertice(vertice)
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 4:
    if importGrafo == False:
      aresta_origem = input(
          "Insira um nome para o ponto turistico origem: ").upper()
      aresta_destino = input(
          "Insira um nome para o ponto turistico destino: ").upper()
      peso = float(input("Insira o valor do peso: "))
      grafo.insereA(aresta_origem, aresta_destino, peso)
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 5:
    if importGrafo == False:
      nome_ponto = input(
          "Insira um nome para o ponto turistico que você deseja remover: "
      ).upper()
      grafo.removerVertice(nome_ponto)
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 6:
    if importGrafo == False:
      aresta_origem = input(
          "Digite o ponto de origem que deseja remover da aresta: ").upper()
      aresta_destino = input(
          "Digite o ponto de destino que deseja remover da aresta: ").upper()
      grafo.removeA(aresta_origem, aresta_destino)
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 7:
    if importGrafo == False:
      print("Mostrando o conteúdo do arquivo txt:\n")
      with open("grafo.txt", "r") as arquivo:
        linhas = arquivo.read()
        print(linhas)
      arquivo.close()
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 8:
    if importGrafo == False:
      grafo.show()
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 9:
    if importGrafo == False:
      if grafo.conexo() == 1:
        print("O Grafo de pontos turísticos e estações de metrô é conexo.\n")
      elif grafo.conexo() == 0:
        print(
            "O Grafo de pontos turísticos e estações de metrô é desconexo.\n")
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 10:
    if importGrafo == False:
      origem = input("Digite o ponto de origem: ").upper()
      destino = input("Digite o ponto de destino: ").upper()
      #caminho, soma_rotulos = grafo.dijkstra(origem, destino)
      grafo.dijkstra(origem, destino)
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")

  elif opcao == 11:
    if importGrafo == False:
      ponto = input("Digite o ponto para saber o grau dele: ").upper()
      #caminho, soma_rotulos = grafo.dijkstra(origem, destino)
      grau = grafo.grauVertice(ponto)
      if grau is not None:
        print(f'O grau do ponto {ponto} é {grau}')
      else:
        print("\nO ponto inserido é inexistente")
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")
      
  elif opcao == 12:
    if importGrafo == False:
      arvore_minima, soma_pesos = grafo.kruskal()
  
      print("\nÁrvore Geradora Mínima:")
      for aresta in arvore_minima:
        ponto1, ponto2, peso = aresta
        print(f"{ponto1.ponto} --- {ponto2.ponto} || PESO = {peso} km")
      print(f"\nA soma dos pesos da Árvore Geradora Mínima é {soma_pesos:.2f} km")
    else:
      print("Primeiramente, insira os dados no grafo (opção 1)")


def main():
  while True:
    print("\n-------------- GRAFO PONTOS TURISTICOS --------------\n")
    print("1 - Ler dados do arquivo grafo.txt")
    print("2 - Gravar dados no arquivo grafo.txt")
    print("3 - Inserir vértice")
    print("4 - Inserir aresta")
    print("5 - Remove vértice")
    print("6 - Remove aresta")
    print("7 - Mostrar conteúdo do arquivo")
    print("8 - Mostrar grafo")
    print("9 - Apresentar a conexidade do grafo")
    print("10 - Caminho minino")
    print("11 - Grau do vertice")
    print("12 - Árvore de custo minimo")
    print("0 - Encerrar a aplicação\n")

    opcao = int(input("Selecione uma opção do menu: "))
    if opcao == 0:
      break
    menu(opcao)


main()
