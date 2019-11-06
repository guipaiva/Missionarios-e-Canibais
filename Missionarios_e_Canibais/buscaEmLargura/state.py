'''
    Esta classe possui os seguintes atributos:
        1 - marginLeft : lista de 2 posições, formada por uma lista enviada como parametro ao construtor da nossa classe. Primeira posição indica o número de missionários e a segunda o número de canibais na margem esquerda do rio
        2 - marginRight :análogo ao atributo 1
        4 - boat : barco, indica o lado em que o barco se encontra. "0" caso esteja na margem esquerda, "1" caso contrário
        5 - parent : elemento que antecede a determinado nó. Pai de um nó
        6 - filhos : lista de filhos de um nó

    A presente classe tem os seguintes métodos:
        1 - verificaEstado(self) : Verifica se determinado estado é válido através de comparações
            Este métdodo retorna False caso:
                1.1. Um movimento/avanço para o próximo estado faça com que o número de canibais em uma das margens seja maior que o número de missionários na mesma margem (primeiro if).
                1.2. Um movimento/avanço para o próximo estado faça com que o número de canibais/missionários em uma das margens seja negativo
            Retorna True caso:
                1.3. O movimento realizado seja válido, ou seja gere um dos estados válidos presente no arquivo "descrevendo o problema.txt"

        2 - objetivo(self): Verfica se o estado atual é o estado meta:
            2.1. O método retorna True caso o número de missionários e canibais na margem direita("1") seja igual a 3
            2.2. O método retorna False caso a condição acima não seja atingida

        3 - expandeEstados(self):
            3.1. Cria uma matriz que armazena possiveis movimentos (ver arquivo: "descrevendo o problema.txt")
            3.2. Define para que lado o barco vai, o barco sempre vai para o lado contrário ao lado atual
            3.3. Faz uma iteração com i indo de 0 a 5. A cada iteração um possível movimento(operacao) é testado, a fim de criar um novo estado.
            3.4. Após ser realizado um movimento é criado um novo estado, chamado filho
            3.5. Salva o pai desse filho gerado (nó atual = self)
            3.6. Verifica se esse novo nó (filho) não viola as condições do problema (busca em largura, verifica o valor primeiro pra depois expandir aquele nó)
            3.7. Se o estado for válido adiciona ele na lista filhos, para que o mesmo possa ser expandido depois
'''
class State():
    def __init__(self,marginLeft, marginRight,boat):
        self.marginLeft = marginLeft
        self.marginRight = marginRight
        self.boat = boat
        self.parent = None
        self.filhos = []


    def verificaEstado(self):
        if(self.marginLeft[0] > 0 and self.marginLeft[1] > self.marginLeft[0]):
            return False #O número de missionários na respectiva margem esquerda é maior que 0 e menor que o número de canibais na mesma margem
        if(self.marginRight[0] > 0 and self.marginRight[1] > self.marginRight[0]):
            return False #Análogo a linha de cima
        if(self.marginLeft[0] < 0 or self.marginLeft[1] < 0 or self.marginRight[0]<0 or self.marginLeft[1]<0):
            return False #Um movimento para outro margem (um novo estado) jamais pode fazer com que o número de canibais/missionários em uma das margens seja negativo
        else:
            return True #nenhum dos movimentos ferem as regras do problema

    def objetivo(self):
        if((self.marginRight[0]==3 and self.marginRight[1]==3 ) and self.boat ==1):
            return True #objetivo desejado
        else:
            return False

    def expandeEstados(self):
        operacoes = [[2,0],[0,2],[1,1],[0,1],[1,0]]
        boat = int(not(self.boat))#se o barco está em uma margem, sua nova margem só pode ser a contrária
        for i in range(5): #O objetivo aqui é gerar novos estados, realizando os movimentos armazenados na matriz "operacoes"
            if (boat==0):
                missionarioRight = self.marginRight[0] - operacoes[i][0]
                canibalRight = self.marginRight[1] - operacoes[i][1]
                missionarioLeft = self.marginLeft[0] + operacoes[i][0]
                canibalLeft = self.marginLeft[1] + operacoes[i][1]
            else:
                missionarioRight = self.marginRight[0] + operacoes[i][0]
                canibalRight = self.marginRight[1] + operacoes[i][1]
                missionarioLeft = self.marginLeft[0] - operacoes[i][0]
                canibalLeft = self.marginLeft[1] - operacoes[i][1]

            filho = State([missionarioLeft,canibalLeft], [missionarioRight,canibalRight],boat) #cria um objeto filho do tipo State
            filho.parent = self #o pai do objeto filho é o objeto atual
            if filho.verificaEstado(): #se o estado do objeto filho for válido
                self.filhos.append(filho) #adicione ele na árvore