class View():

    def saudacao():
        print('\n\n')
        print('-' * 40)
        print('-')
        print('-', '  Zombie Dice 🧠')
        print('-')
        print('-' * 40)

    def embaralhando_jogadores():
        print('')
        print('Embaralhando a ordem dos jogadores...')

    def mostrar_ordem_jogadores(jogadores):
        print('')
        print('Ordem dos jogadores:')
        for jogador in jogadores:
            print('- ', jogador['nome'])

    def mostrar_jogador_da_vez(jogador):
        print('')
        print('-' * 40)
        print('-')
        print('-', f'Atenção!! Vez de: ', jogador['nome'])
        print('-')
        print('-' * 40)

    def mostrar_msg_perda(jogador):
        print('')
        print('Ah não, ', jogador['nome'], ' levou 3 tiros e perdeu a vez...')

    def mostrar_msg_vencedor(jogador):
        print('')
        print('-' * 40)
        print('-')
        print('-', f'Parabéns!! ', jogador['nome'], ' ganhou o jogo!!')
        print('-')
        print('-' * 40)




    def mostrar_pontos(c, p, t, nome):  # ------------------------------------------------Mostrando pontos---
        print('\n\n','*' * 5, f'Pontuação atual de {nome:10}')
        print(f'{"Cérebro":^10}|{"Passos":^10}|{"Tiros":^10}')
        print(f'{c:^10}|{p:^10}|{t:^10}')
        pass







    def encerramento_jogo():
        print('')
        print('-' * 40)
        print('-')
        print('-', '  Jogo Encerrado')
        print('-')
        print('-' * 40)