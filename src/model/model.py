from random import shuffle, choice
from src.view.view import View

class Modelos():

    def coletar_jogadores():

        quantia_jogadores = int(input('\nQuantos jogadores nessa partida?\n   '))

        if quantia_jogadores < 2:
            raise Exception("Precisa de 2 ou mais jogadores")
        
        lista_jogadores = []

        print('')
        for a in range(quantia_jogadores):
            nome = str(input(f'Nome do jogador {a + 1}: '))
            lista_jogadores.append(nome)

        return lista_jogadores
    

    def sortear_ordem_jogadores(lista_jogadores):
        View.embaralhando_jogadores()
        shuffle(lista_jogadores)
        return lista_jogadores












    def criar_tubo():  # ----------------------------------------------------Tubo original com os 13 dados---
        tubo_f = ['verde', 'verde', 'verde', 'verde', 'verde', 'verde', 'amarelo', 'amarelo', 'amarelo', 'amarelo', 'vermelho', 'vermelho', 'vermelho']
        return tubo_f

    def definir_faces():  # ---------------------------------------------Faces conforme as cores dos dados---
        verde = ('cérebro', 'cérebro', 'cérebro', 'passos', 'passos', 'tiro')
        amare = ('cérebro', 'cérebro', 'passos', 'passos', 'tiro', 'tiro')
        verme = ('cérebro', 'passos', 'passos', 'tiro', 'tiro', 'tiro')
        return verde, amare, verme



    def jogar_dados(tubo_atual, d_verde, d_amare, d_verme):  # ---------------Jogando os dados disponiveis---
        dado = choice(tubo_atual)
        if dado == 'verde':
            face = choice(d_verde)  # dado verde
        elif dado == 'amarelo':
            face = choice(d_amare)  # dado amarelo
        else:
            face = choice(d_verme)  # dado vermelho
        return dado, face

    def contar_pontos(dados_round, faces_round):  # --------------------------Salvando os pontos da rodada---
        dado_remover = []
        pontos = []

        # c = int(0)
        # p = int(0)
        # t = int(0)
        
        for a in range(3):
            if faces_round[a] == 'cérebro':
                dado_remover.append(dados_round[a])
                c = c + 1
            elif faces_round[a] == 'tiro':
                dado_remover.append(dados_round[a])
                t = t + 1
            else:
                p = p + 1
        return c, p, t, dado_remover

def mostrar_pontos(c, p, t, nome):  # ------------------------------------------------Mostrando pontos---
    print('\n\n','*' * 5, f'Pontuação atual de {nome:10}')
    print(f'{"Cérebro":^10}|{"Passos":^10}|{"Tiros":^10}')
    print(f'{c:^10}|{p:^10}|{t:^10}')
    pass

def retirar_dados_do_tubo(dado_tirar, tubo):  # --------------------------------Retirando dados do tubo---

    print(f'Retirando {len(dado_tirar)} dado: {dado_tirar} \n Do tubo {len(tubo)} {tubo}\n')

    for a in range(len(dado_tirar)):
        print(a,' : ',dado_tirar[a],'\n') 
        x = tubo.index(dado_tirar[a])
        tubo.pop(x)
    
    return tubo

def verificar_pontos(cer,tir):  # -----------------------------------------------Verificando os pontos---
    if cer >= 13:
        return True
    elif tir >= 3:
        return True
    else:
        pass
