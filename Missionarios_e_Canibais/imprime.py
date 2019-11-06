'''
    Essa classe serve unicamente para imprimir nossa solução. Ela faz isso recebendo no construtor o objeto missionariosCanibais do tipo
    buscaSolucao, após isso é chamado através desse objeto o método solucao(descrito detalhadamente no arquivo buscaSolucao.py) que resumidamente monta nossa árvore e salva o caminho que nos
    conduz a solução. Após isso iteramos sobre essa solução, fazemos operações entre o estado atual e o pai, para saber que movimento nos levou a determinada margem
    e imprimimos cada estado da solução .
'''
from buscaSolucao import *

class Imprime():
    def __init__(self,missionariosCanibais):
        self.missionariosCanibais = missionariosCanibais
    def imprime(self):
        self.missionariosCanibais.solucao()
        print("\t\tConfiguração de estados válidos\n")
        i=0
        for estado in self.missionariosCanibais.caminho: #itera sobre a lista caminho da classe BuscaSolucao, que contém a solução do problema armazenada
            if(i!=0):
                print("-->Saem no barco:")
                if(int(estado.parent.marginLeft[0])>int(estado.marginLeft[0])):#missionários saíram do lado esquerdo
                    print("\t"+str(abs(int(estado.parent.marginLeft[0])-int(estado.marginLeft[0])))+" missionário(s) rumo a margem direita")
                elif(int(estado.parent.marginLeft[0])!=int(estado.marginLeft[0])): #missionários saíram do lado direito para o esquerdo.
                    print("\t"+str(abs(int(estado.parent.marginRight[0])-int(estado.marginRight[0])))+" missionário(s) rumo a margem esquerda")
                if(int(estado.parent.marginLeft[1])>int(estado.marginLeft[1])):#canibais saíram do lado esquerdo
                    print("\t"+str(abs(int(estado.parent.marginLeft[1])-int(estado.marginLeft[1])))+" canibal(is) rumo a margem direita")
                elif(int(estado.parent.marginLeft[1])!=int(estado.marginLeft[1])): #canibais saíram do lado direito para o esquerdo.
                    print("\t"+str(abs(int(estado.parent.marginRight[1])-int(estado.marginRight[1])))+" canibal(is) rumo a margem esquerda")
                print("\t* Gerando assim o estado "+str(i+1)+":")
            else: print("* Estado de entrada:")

            print("\t\t"+str(estado.marginLeft[0]) + " missionários e " + str(estado.marginLeft[1]) + " canibais na margem esquerda do rio.")
            print("\t\t"+str(estado.marginRight[0]) + " misisonários e " + str(estado.marginRight[1]) + " canibais na margem direita do rio.\n")
            i = i+1