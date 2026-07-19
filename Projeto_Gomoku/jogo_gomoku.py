import random
from time import sleep

class Tabuleiro:
    def __init__(self):
        self._matriz = []
        self.__lista = []
        self.vazios = 0
    
    # Um método para criar uma matriz de 19 linhas e 19 colunas
    def _criar_matriz(self): 
        self._matriz = []
        for i in range(19):
            self.__lista = []
            for j in range(19):
                self.__lista.append('□')
            self._matriz.append(self.__lista)
        
        return self._matriz

    # Função para printar o tabuleiro formatado
    def mostrar_tabuleiro(self):
        print("     ", end='')
        for j in range(19):
            print(f'{j + 1:<5}', end='')
        print()

        for i, linha in enumerate(self._matriz):
            print(f'{i + 1:<2}', linha)
        return None
    
    def contar_vazios(self, tabuleiro):
        tabuleiro.vazios = 0
        for lista in tabuleiro._matriz:
            for elemento in lista:
                if elemento == '□':
                    tabuleiro.vazios += 1

class Pecas:
    def __init__(self):
        self._peca_jogador = '⛾'
        self._peca_oponente = '⛝'

class Jogador:
    def __init__(self):
        self.pecas = Pecas()
        self.contador_jogador = 0
        self.vitoria_jogador = False

    # Função para posicionar a peça do jogador
    def posicionar_peca_jogador(self, linha, coluna, tabuleiro_modificado):
        matriz = tabuleiro_modificado._matriz
        matriz[linha][coluna] = self.pecas._peca_jogador
        return tabuleiro_modificado.mostrar_tabuleiro()

    # Verifica se o jogador tem peças consecutivas em determinada posição
    def __verificacao_pecas_jogador(self, matriz, lin, col):
        '''Método para verificar a vitória em cada instância da verificação dos métodos'''
        if matriz[lin][col] == self.pecas._peca_jogador:
            self.contador_jogador += 1
                        
        if matriz[lin][col] == '□' or matriz[lin][col] == self.pecas._peca_oponente:
            self.contador_jogador = 0

        if self.contador_jogador == 5:
            self.vitoria_jogador = True
    
    def msg_vitoria_jogador(self, modo_jogo):
        if modo_jogo == 1:
            return 'Parabéns, Você venceu o computador!'
        else:
            return 'Vitória do Jogador 1'

    def vericacao_vitoria_jogador(self, tabuleiro_modificado):
        ''' Método para verificar em que posição as peças estão e se formaram 5 para a vitória '''
        # Verificação para ver se o jogador venceu em alguma linha
        matriz = tabuleiro_modificado._matriz
        self.contador_jogador = 0
        for lin in range(len(matriz)):
            for col in range(len(matriz)):
               self.__verificacao_pecas_jogador(matriz, lin, col)
        
        # Verificação para ver se o jogador venceu em alguma coluna
        self.contador_jogador = 0
        for col in range(len(matriz)):
            for lin in range(len(matriz)):
                self.__verificacao_pecas_jogador(matriz, lin, col)
        
        # Verificação para ver se o jogador venceu na diagonal principal ou na diagonal principal para baixo
        self.contador_jogador = 0
        for contador in range(14):
            for lin in range(len(matriz)):
                for col in range(len(matriz)):
                    if lin == col + contador:
                        self.__verificacao_pecas_jogador(matriz, lin, col)
  
        # Verificação da diagonal principal para a direita
        self.contador_jogador = 0
        for contador in range(14):
            for lin in range(len(matriz)):
                for col in range(len(matriz)):
                    if col == lin + contador and lin - col != 0:
                        self.__verificacao_pecas_jogador(matriz, lin, col)
        
        # Verificação para ver se o jogador venceu na diagonal secundária
        self.contador_jogador = 0
        # Verificação da diagonal secundária para a esquerda
        for contador in range(18, 4, -1):
            for lin in range(0, len(matriz), 1):
                for col in range(len(matriz) - 1, 4, -1):
                    if col + lin == contador:
                        self.__verificacao_pecas_jogador(matriz, lin, col)
        
        # Verificação da diagonal secundária para baixo
        self.contador_jogador = 0
        for contador in range(19, 33):
            for lin in range(0, len(matriz), 1):
                for col in range(len(matriz) - 1, 4, -1):
                    if col + lin == contador:
                        self.__verificacao_pecas_jogador(matriz, lin, col)


class Oponente:
    def __init__(self):
        self.pecas = Pecas()
        self.contador_oponente = 0
        self.vitoria_oponente = False
    
    def posicionar_peca_oponente(self, linha, coluna, tabuleiro_modificado):
        matriz = tabuleiro_modificado._matriz
        if matriz[linha][coluna] == '□':
                matriz[linha][coluna] = self.pecas._peca_oponente
                return tabuleiro_modificado.mostrar_tabuleiro()
        
        else:
            return 'Jogada Inválida'
    
    def __verificacao_pecas_oponente(self, matriz, lin, col):
        if matriz[lin][col] == self.pecas._peca_oponente:
            self.contador_oponente += 1
                    
        if matriz[lin][col] == '□' or matriz[lin][col] == self.pecas._peca_jogador:
            self.contador_oponente = 0

        if self.contador_oponente == 5:
            self.vitoria_oponente = True

    def msg_vitoria_oponente(self, modo_jogo):
        if modo_jogo == '1':
            return 'Vitória do Computador'
        else:
            return 'Vitória do Jogador 2'
        
    def verificacao_vitoria_oponente(self, tabuleiro_modificado):
        # Verificação para ver se o oponente venceu em alguma linha
        matriz = tabuleiro_modificado._matriz
        self.contador_oponente = 0
        for lin in range(len(matriz)):
            for col in range(len(matriz)):
               self.__verificacao_pecas_oponente(matriz, lin, col)

        # Verificação para ver se o oponente venceu em alguma coluna
        self.contador_oponente = 0
        for col in range(len(matriz)):
            for lin in range(len(matriz)):
                self.__verificacao_pecas_oponente(matriz, lin, col)

        # Verificação para ver se o oponente venceu na diagonal principal
        self.contador_oponente = 0
        for contador in range(14):
            for lin in range(len(matriz)):
                for col in range(len(matriz)):
                    # Verificação da diagonal principal para baixo
                    if lin == col + contador:
                        self.__verificacao_pecas_oponente(matriz, lin, col)
                    
        # Verificação da diagonal principal para a direita
        for contador in range(14):
            for lin in range(len(matriz)):
                for col in range(len(matriz)):
                    if col == lin + contador and lin - col != 0:
                        if col == lin + contador:
                            self.__verificacao_pecas_oponente(matriz, lin, col)
        
        # Verificação da diagonal secundária para a esquerda
        for contador in range(18, 4, -1):
            for lin in range(0, len(matriz), 1):
                for col in range(len(matriz) - 1, 4, -1):
                    if col + lin == contador:
                        self.__verificacao_pecas_oponente(matriz, lin, col)
        
        # Verificação da diagonal secundária para baixo
        for contador in range(19, 33):
            for lin in range(0, len(matriz), 1):
                for col in range(len(matriz) - 1, 4, -1):
                    if col + lin == contador:
                        self.__verificacao_pecas_oponente(matriz, lin, col)
    
class Pontuacao:
    def __init__(self):
        self.pontuacao_jogador = 0
        self.pontuacao_oponente = 0

    def pontuar_jogador(self):
            '''Faz o Jogador pontuar'''
            self.pontuacao_jogador += 1
            return self.pontuacao_jogador
        
    def pontuar_oponente(self):
            '''Faz o Oponente pontuar'''
            self.pontuacao_oponente += 1
            return self.pontuacao_oponente


class Jogo:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogador = Jogador()
        self.oponente = Oponente()
        self.pontuacao = Pontuacao()

    def __apresentacao_jogo(self):
        '''Apresentação do Início do Jogo '''
        print('\nO jogo começará em alguns instantes...\n')
        sleep(3)
        print('-=-' * 33)
        print('\033[36mGomoku\033[m'.center(99))
        print(f'{'-=-' * 33}\n')
        return None

    def __verificacao_escolha_jogador(self, modo_jogo, lin, col):
        '''Faz a subtração das linhas e colunas de forma a induzir o jogador a escolher de 1 a 19 para linhas e colunas, invés de 0 a 18. Também verifica o modo de jogo para printar uma mensagem adequada'''
        if modo_jogo == 1:
            print(f'\nO jogador escolheu a linha {lin} e a coluna {col}')
            lin -= 1
            col -= 1  
            if self.tabuleiro._matriz[lin][col] == '□':
                self.jogador.posicionar_peca_jogador(lin, col, self.tabuleiro)
                return True
                
            else:
                return False
        
        else:
            print(f'\nO jogador1 escolheu a linha {lin} e a coluna {col}')
            lin -= 1
            col -= 1  
            if self.tabuleiro._matriz[lin][col] == '□':
                self.jogador.posicionar_peca_jogador(lin, col, self.tabuleiro)
                return True
            
            else:
                print('\nJogada Inválida, Tente Novamente!')
                return False


    def __verificacao_escolha_oponente(self, modo_jogo, lin, col):
        '''Faz a subtração das linhas e colunas de forma a induzir o oponente a escolher de 1 a 19 para linhas e colunas, invés de 0 a 18. Também verifica o modo de jogo para printar uma mensagem adequada'''
        if modo_jogo == 1:
            print(f'\nO computador escolheu a linha {lin} e a coluna {col}')
            lin -= 1
            col -= 1  
            if self.tabuleiro._matriz[lin][col] == '□':
                self.oponente.posicionar_peca_oponente(lin, col, self.tabuleiro)
                return True
            else:
                return False

        else:
            print(f'\nO jogador2 escolheu a linha {lin} e a coluna {col}')
            lin -= 1
            col -= 1  
            if self.tabuleiro._matriz[lin][col] == '□':
                self.oponente.posicionar_peca_oponente(lin, col, self.tabuleiro)
                return True
            else:
                print('\nJogada Inválida, Tente Novamente!')
                return False

    def turno_jogador(self, modo_jogo, lin, col):     
        # Verificação para ver se a jogada é válida ou inválida
        if (lin < 1 or lin > 19) or (col < 1 or col > 19):
            print('Coordenada Inválida')
            return False
        else:
            if self.__verificacao_escolha_jogador(modo_jogo, lin, col):
                return True
            else:
                return False
            
    def turno_oponente(self, modo_jogo, lin, col):
        # Verificação para ver se a jogada do oponente é válida ou inválida
        if (lin < 1 or lin > 19) or (col < 1 or col > 19):
            print('Coordenada Inválida')
            return False
        else:
            if self.__verificacao_escolha_oponente(modo_jogo, lin, col):
                return True
            else:
                return False
        
    def processar_inicio_jogo(self):
        ''' Métodos de inicialização do jogo '''
        self.tabuleiro._criar_matriz()
        # Apresentação do nome do Jogo
        self.__apresentacao_jogo()
        # Mostra o tabuleiro formatado em matriz
        self.tabuleiro.mostrar_tabuleiro()
        return None

    def recriar_jogo(self):
        # Recria o jogo inteiro após
            self.tabuleiro._criar_matriz()
            self.__apresentacao_jogo()
            self.tabuleiro.mostrar_tabuleiro()
            self.jogador.vitoria_jogador = False
            self.oponente.vitoria_oponente = False
            return None
        
        
    def jogar(self, modo_jogo):
        if modo_jogo == 1:
            self.processar_inicio_jogo()
            turno = 0
            while True:
                turno += 1
                print(f'\nTurno {turno} do jogador:')
                # Escolhas do jogador para linha e coluna
                while True:
                    escolha_jogador_linha = int(input('\nEscolha um número de 1 a 19 para definir a linha que você quer jogar: '))
                    escolha_jogador_coluna = int(input('Escolha um número de 1 a 19 para definir a coluna que você quer jogar: '))   

                    if self.turno_jogador(modo_jogo, escolha_jogador_linha, escolha_jogador_coluna):
                        break
                    else:
                        continue
                    
                    # Verifica se o jogador venceu em alguma posição
                self.jogador.vericacao_vitoria_jogador(self.tabuleiro)
       
                if self.jogador.vitoria_jogador:
                    # Printa uma mensagem de vitória se o jogador tiver vencido
                    print(f'\n{self.jogador.msg_vitoria_jogador(modo_jogo)}')
                    # Faz o jogador pontuar no placar
                    self.pontuacao.pontuar_jogador()
                    # Pergunta ao jogador se ele irá querer continuar o jogo após vencer
                    continuacao = input('Deseja Continuar [s/n]? ')
                    
                    if continuacao.lower() == 's':
                        self.recriar_jogo()
                        # Mostra o placar
                        print(f'Placar: Jogador: {self.pontuacao.pontuacao_jogador} VS Computador: {self.pontuacao.pontuacao_oponente}')
                        turno = 0
                        continue
                    else:
                        break

                print(f'Turno {turno} do computador')
                
                while True:
                    escolha_PC_linha = random.randint(1, 19)
                    escolha_PC_coluna = random.randint(1, 19)
                    
                    if self.turno_oponente(modo_jogo, escolha_PC_linha, escolha_PC_coluna):
                        break
                    else:
                        continue           
                    
                self.oponente.verificacao_vitoria_oponente(self.tabuleiro)

                if self.oponente.vitoria_oponente:
                    print(f'\n{self.oponente.msg_vitoria_jogador(modo_jogo)}')
                    self.pontuacao.pontuar_oponente()
                    continuacao = input('Deseja Continuar [s/n]? ')
                    if continuacao.lower() == 's':
                        self.recriar_jogo()
                        print(f'Placar: Jogador: {self.pontuacao.pontuacao_jogador} VS Computador: {self.pontuacao.pontuacao_oponente}')
                        turno = 0
                        continue
                    else:
                        break
                
                # Sistema de Empate
                self.tabuleiro.contar_vazios(self.tabuleiro)
                if self.tabuleiro.vazios == 0 and self.jogador.vitoria_jogador == False and self.oponente == False:
                    print('Empate!')
                    continuacao = input('Deseja Continuar [s/n]? ')
                    if continuacao.lower() == 's':
                        self.recriar_jogo()
                        print(f'Placar: Jogador1: {self.pontuacao.pontuacao_jogador} VS Jogador2: {self.pontuacao.pontuacao_oponente}')
                        turno = 0
                        continue

            print(f'Placar Final: Jogador: {self.pontuacao.pontuacao_jogador} VS Computador: {self.pontuacao.pontuacao_oponente}')
        
        elif modo_jogo == 2:
            self.processar_inicio_jogo()
            turno = 0
            while True:
                turno += 1
                print(f'\nTurno {turno} do jogador1:')
                # Escolhas do jogador para linha e coluna
 
                while True:
                    escolha_jogador1_linha = int(input('\nEscolha um número de 1 a 19 para definir a linha que você quer jogar: '))
                    escolha_jogador1_coluna = int(input('Escolha um número de 1 a 19 para definir a coluna que você quer jogar: '))      
                    # Verificação para ver se a jogada é válida ou inválida

                    if self.turno_jogador(modo_jogo, escolha_jogador1_linha, escolha_jogador1_coluna):
                        break
                    else:
                        continue
                    
                    # Verifica se o jogador venceu em alguma posição
                self.jogador.vericacao_vitoria_jogador(self.tabuleiro)
       
                if self.jogador.vitoria_jogador:
                    # Printa uma mensagem de vitória se o jogador tiver vencido
                    print(f'\n{self.jogador.msg_vitoria_jogador(modo_jogo)}')
                    # Faz o jogador pontuar no placar
                    self.pontuacao.pontuar_jogador()
                    # Pergunta ao jogador se ele irá querer continuar o jogo após vencer
                    continuacao = input('Deseja Continuar [s/n]? ')
                    if continuacao.lower() == 's':
                        self.recriar_jogo()
                        print(f'Placar: Jogador1: {self.pontuacao.pontuacao_jogador} VS Jogador2: {self.pontuacao.pontuacao_oponente}')
                        turno = 0
                        continue
                    else:
                        break
                
                print(f'\nTurno {turno} do jogador2:')

                while True:
                    escolha_jogador2_linha = int(input('\nEscolha um número de 1 a 19 para definir a linha que você quer jogar: '))
                    escolha_jogador2_coluna = int(input('Escolha um número de 1 a 19 para definir a coluna que você quer jogar: '))
                    
                    if self.turno_oponente(modo_jogo, escolha_jogador2_linha, escolha_jogador2_coluna):
                        break
                    else:
                        continue          
                    
                self.oponente.verificacao_vitoria_oponente(self.tabuleiro)

                if self.oponente.vitoria_oponente:
                    print(f'\n{self.oponente.msg_vitoria_oponente(modo_jogo)}')
                    self.pontuacao.pontuar_oponente()
                    continuacao = input('Deseja Continuar [s/n]? ')
                    if continuacao.lower() == 's':
                        self.recriar_jogo()
                        print(f'Placar: Jogador1: {self.pontuacao.pontuacao_jogador} VS Jogador2: {self.pontuacao.pontuacao_oponente}')
                        turno = 0
                        continue
                    else:
                        break
            
                # Sistema de Empate
                self.tabuleiro.contar_vazios(self.tabuleiro)
                if self.tabuleiro.vazios == 0 and (self.jogador.vitoria_jogador == False and self.oponente == False):
                    print('Empate!')
                    continuacao = input('Deseja Continuar [s/n]? ')
                    if continuacao.lower() == 's':
                        self.recriar_jogo()
                        print(f'Placar: Jogador1: {self.pontuacao.pontuacao_jogador} VS Jogador2: {self.pontuacao.pontuacao_oponente}')
                        turno = 0
                        continue

            print(f'Placar Final: Jogador1: {self.pontuacao.pontuacao_jogador} VS Jogador2: {self.pontuacao.pontuacao_oponente}')
        
        else:
            print('Modo de Jogo Inválido')

jogo = Jogo()
modo_jogo = int(input("Digite [1] para jogar com um computador ou digite [2] para jogar com outro jogador: "))

jogo.jogar(modo_jogo)



