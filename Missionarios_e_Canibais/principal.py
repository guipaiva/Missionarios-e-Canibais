'''
    A clase Principal tem por objetivo inicializar o nosso problema. Ela faz isso da seguinte forma:
        1 - Cria um objeto missionariosCanibais do tipos BuscaSolucao, envia como parâmetros duas listas e a posição do barco (0 para esquerda e 1 para a direita). A primeira lista se
            refere a quantidade de pessoas na margem esquerda do rio, já a segunda se refere ao número de pessoas na margem direita, sendo que a primeira posição destas listas se refere
            aos missionários, e a segunda possição aos canibais. Optamos para que os estados sejam enviados aqui para facilitar a mudança dos mesmos (caso desejado), haja vista que esse arquivo
            é mais limpo do ponto de vista visual. Além de tudo, futuramente, quando for desejado usar outro método, basta alterar o caminho do arquivo selecionado (desde que os métodos invocados aqui possuam a mesma assinatura)
        2 - Por último é criado um objeto imprime que chama o método imprime da classe Imprime, que imprime nossa soluçãoptimize
'''
import sys
sys.path.append("buscaEmLargura") #adiciona o caminho buscaEmLargura no caminho padrão para que as classes abaixo possam ser importadas
from buscaSolucao import *
from imprime import *
from state import *
class Principal():
    def main():
        missionariosCanibais = BuscaSolucao([3,3],[0,0],0) #Configuração Inicial
        imprime = Imprime(missionariosCanibais)
        imprime.imprime()
    if __name__ == '__main__':
        main()