'''
    Essa classe se concentra em encontrar a solução para o nosso problema, para tal os seguintes passos são tomados:
        1 - É criado uma lista tree (ela será nossa árvore). O primeiro elemento dessa lista será nosso estado atual, por esse motivo o mesmo é inicializado da forma vista abaixo
        2 - Método solucao(self):
            2.1. Itera sobre a lista (nossa árvore é construída através de uma lista), a cada iteração node recebe um item dessa lista
            2.2. Se o nó (item da árvore) que estamos analisando tiver alcançado nosso objetivo:
                2.2.1. Salvamos ele na nossa lista caminho (ela guarda nossa solução)
                2.2.2. Enquanto o parent do nosso nó for diferente de none, inserimos o pai do nosso nó na cabeça da nossa lista, e atualiazamos o nosso nó (nó =  pai do nó, lembrando estamos fazendo um caminho inverso, da folha até a raiz)
            2.3 Se o nó analisado não for nosso objetivo ainda:
                2.3.1. Expanda esse nó, através do método expandeEstados.
                2.3.2. Adiciona na ávore os nós gerados pelo método expandeEstados
'''

from state import *
class BuscaSolucao():
    def __init__(self,marginLeft,marginRight,boat):
        self.caminho = None #até agora não temos solução
        self.tree = [State(marginLeft,marginRight,boat)] #inicializa nossa árvore com um nó do tipo State

    def solucao(self):
        for node in self.tree: #itera sobre os elementos da árvore
            if(node.objetivo()): #se o nó da nossa árvore for o nosso estado meta, faça
                self.caminho= [node] #salve em caminho nosso nó atual
                while node.parent: #agora precisamos salvar o caminho reverso, enquanto o nó analisado tiver o parent diferente de none
                    self.caminho.insert(0,node.parent) #armazene parent na cabeça da nossa lista que contém a solução
                    node = node.parent #nosso nó agora é o parent do nó anterior
                break;
            else:
                node.expandeEstados() #nosso nó não é a solução, mas é válido, crie um novo nó na árvore
                self.tree.extend(node.filhos) #adicione este nó na árvore