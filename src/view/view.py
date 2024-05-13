class View():

    def saudacao():
        print('\n\n')
        print('-' * 40)
        print('-')
        print('-', '  Zombie Dice 🧠 🎲')
        print('-')
        print('-' * 40)

    def embaralhando_jogadores():
        print('')
        print('Embaralhando a ordem dos jogadores...')

    def mostrar_ordem_jogadores(jogadores):
        print('')
        print('Ordem dos jogadores:')
        print('')
        for jogador in jogadores:
            print('- ', jogador['nome'])

    def mostrar_jogador_da_vez(jogador):
        print('')
        print('-' * 40)
        print('-')
        print('-', f' Atenção!! Vez de: ', jogador['nome'])
        print('-')
        print('-' * 40)

    def mostrar_resultado_jogada(rodada, tiros, cerebros):
        print('')
        print('.  Resultado da jogada: ') 
        print('.')
        for i in range(3):
            print(f'.  Dado: {rodada[i][0]} - Face: {rodada[i][1]}')
        print('.')
        print('. ⚠️  - Tiros: ', tiros.count('tiro'), 'x tiro') 
        print('. ⚠️  - Cerebros: ', cerebros.count('cerebro'), 'x cerebro') 

    def mostrar_msg_passa_vez(jogador):
        print('')
        print(' ❕ ', jogador['nome'], ' passou a vez ❕')

    def mostrar_msg_perda(jogador):
        print('')
        print('Ah não, ', jogador['nome'], ' levou 3 tiros e perdeu a vez...')

    def mostrar_msg_vencedor(jogador):
        print('')
        print('-' * 40)
        print('- 🏆')
        print('- 🏆 ', 'Parabéns ', jogador['nome'],'!!')
        print('- 🏆  Você ganhou o jogo!!')
        print('- 🏆')
        print('-' * 40)

    def encerramento_jogo():
        print('')
        print('-' * 40)
        print('-')
        print('-', ' ☠️   Jogo Encerrado')
        print('-')
        print('-' * 40)