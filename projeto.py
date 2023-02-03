from random import shuffle, choice
from time import sleep
import os

# ======================================================================================================= #
#   Funções                                                                                               #
# ======================================================================================================= #
def criar_tubo():  # ----------------------------------------------------Tubo original com os 13 dados---
    tubo_f = ['verde', 'verde', 'verde', 'verde', 'verde', 'verde',
              'amarelo', 'amarelo', 'amarelo', 'amarelo',
              'vermelho', 'vermelho', 'vermelho']
    return tubo_f


def definir_faces():  # ---------------------------------------------Faces conforme as cores dos dados---
    verde = ('cérebro', 'cérebro', 'cérebro', 'passos', 'passos', 'tiro')
    amare = ('cérebro', 'cérebro', 'passos', 'passos', 'tiro', 'tiro')
    verme = ('cérebro', 'passos', 'passos', 'tiro', 'tiro', 'tiro')
    return verde, amare, verme


def coletar_jogadores():  # ------------Coleta da quantia e nome dos jogadores, e aleatoriando a ordem---
    lista_nomes = []  # Uma lista para armazenar os jogadores
    qnt_jgdr = int(input('Quantos jogadores nessa partida? '))
    if qnt_jgdr < 2:  # encerrando se não tiver no minino 2 jogadores
        pass
    else:
        for a in range(qnt_jgdr):
            nome = str(input(f'Digite o nome do jogador {a + 1}:'))
            lista_nomes.append(nome)
        shuffle(lista_nomes)
        print('\nOrdem dos jogadores:')
        for a in range(qnt_jgdr):
            print(f'{a + 1}: {lista_nomes[a]}')
    return lista_nomes, qnt_jgdr


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
    c = int(0)
    p = int(0)
    t = int(0)
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
    print('- ' * 20, f'\n- Pontuação atual : {nome:10}')
    print(f'{"Cérebro":^10}|{"Passos":^10}|{"Tiros":^10}')
    print(f'{c:^10}|{p:^10}|{t:^10}')
    print('- ' * 20)


def continuar_jogando():
    op = input('Continuar jogando os dados? s/n  ')
    return op


def retirar_dados_do_tubo(dado_tirar, tub):  # --------------------------------Retirando dados do tubo---
    print(f'Retirando {len(dado_tirar)}: {dado_tirar} \nDo tubo {len(tub)} {tub}')

    for a in range(len(dado_tirar)):
        tub.pop(dado_tirar(a))
    print(f' Tub {tub}') 
    return tub


def verificar_ganhador(cer):  # --------------------------------------------Verificando se há ganhador---
    if cer >= 13:
        return True
    else:
        pass


def verificar_perdedor(tir):  # --------------------------------------------Verificando se há perdedor---
    if tir >= 3:
        return True
    else:
        pass


# ======================================================================================================= #
#   Inicio do código                                                                                      #
# ======================================================================================================= #
tubo = []  # -------------------------------------------------------------Declarando as variáveis locais---
dado_retirar = []
dados_rodada = []
faces_rodada = []
pontos_c = []  # Lista para armazenar a pontuação de cérebros dos jogadores
nomes_jogadores: list[str] # Lista para armazenar o nome dos jogadores

os.system('cls') # ---------------------------------------------------Limpa tela e "começo" da interface---
print('= ' * 6, 'Zombie Dice ', '= ' * 6) # Cabeçalho
nomes_jogadores, quantia_jogadores = coletar_jogadores()

if quantia_jogadores < 2:
    print('Precisa de 2 ou mais jogadores')
else:
    fim = False
    while not fim:
        for i in range(quantia_jogadores):
            tubo = criar_tubo()
            verd, amar, verm = definir_faces()
            print(f'\n- - - Vez de {nomes_jogadores[i]} - - -')

            vez = 's'
            while vez == 's':
                dado_retirar.clear()
                print(f'\nDados no tubo: {len(tubo)}\n{tubo}\n')
                for j in range(3):
                    dado_sorteado, face_sorteada = jogar_dados(tubo, verd, amar, verm)
                    print(f'dado {j + 1}: Cor {dado_sorteado} na face {face_sorteada}')
                    dados_rodada.append(dado_sorteado)
                    faces_rodada.append(face_sorteada)
                ce, pa, ti, dado_retirar = contar_pontos(dados_rodada, faces_rodada)
                mostrar_pontos(ce, pa, ti, nomes_jogadores[i])
                print(f'Dados a ser retirado do tubo: \n{dado_retirar}')
    # -----------------------------------------------------------------------------------Até aki ok


                #retirar_dados_do_tubo(dado_retirar, tubo)
                vez = continuar_jogando()

                pontos_c.append(1)

                x = verificar_ganhador(pontos_c[i])
                y = verificar_perdedor(ti)

                if x:
                    print(f'\n- Jogador: {nomes_jogadores[i]} ganhou!! -')
                    break

                if y:
                    print(f'\n- Jogador: {nomes_jogadores[i]} perdeu!! -')
                    break



print('\n\nJogo encerrado\n\n\n\n')
