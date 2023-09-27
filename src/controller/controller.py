from src.model.model import Modelos
# from src.view.view import View
from time import sleep

class Jogo():
    def apresenta():
        print("testado")
    
    def start():
        tubo = []  # -------------------------------------------------------------Declarando as variáveis locais---
        dado_retirar = []
        dados_rodada = []
        faces_rodada = []
        pontos_c = []  # Lista para armazenar a pontuação de cérebros dos jogadores
        nomes_jogadores: list[str] # Lista para armazenar o nome dos jogadores

        nomes_jogadores, quantia_jogadores = Modelos.coletar_jogadores() # Coletando e sorteando a ordem dos jogadores


        if quantia_jogadores >= 2:

            fim = False
            while fim == False:

                for i in range(quantia_jogadores):

                    tubo = Modelos.criar_tubo()
                    verd, amar, verm = Modelos.definir_faces()

                    vez = 's'
                    while vez == 's':   

                        dado_retirar.clear()
                        dados_rodada.clear()
                        faces_rodada.clear()

                        print('\n\n','*' * 5, f'Vez de {nomes_jogadores[i]}')

                        # print(f'Dados no tubo: {len(tubo)} : {tubo}')

                        for j in range(3):
                            dado_sorteado, face_sorteada = Modelos.jogar_dados(tubo, verd, amar, verm)
                            print(f'dado {j + 1}: Cor {dado_sorteado} na face {face_sorteada}')
                            dados_rodada.append(dado_sorteado)
                            faces_rodada.append(face_sorteada)
                        #print(f'Dados e faces sorteadas: {dados_rodada} : {faces_rodada}\n\n')

                        c, p, t, dado_retirar = Modelos.contar_pontos(dados_rodada, faces_rodada)
                        Modelos.mostrar_pontos(c, p, t, nomes_jogadores[i])
                        print(f'\nDados a ser retirado do tubo: {dado_retirar}\n')

                        #..............................................................................................


                        tubo = Modelos.retirar_dados_do_tubo(dado_retirar, tubo)

                        print(f'Dados no tubo: {len(tubo)} : {tubo}\n')


                        #..............................................................................................


                        vez = input('Continuar jogando os dados? s/n  ')


                        sleep (1)
                        print('*' * 38) # Divisória


                    print('*' * 5, f'{nomes_jogadores[i]} passou a vez')
        


        print('*' * 5, 'Jogo encerrado', '*' * 17, '\n\n') 

        #                retirar_dados_do_tubo(dado_retirar, tubo)
        #                
        #                pontos_c.append(1)
        #
        #                x = verificar_ganhador(pontos_c[i])
        #                y = verificar_perdedor(ti)
        #                
        #
        #                sleep(5) #Espera 5 segundos