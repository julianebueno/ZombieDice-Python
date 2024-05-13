class Modelos():

    def coletar_jogadores():
        while True:
            quantia_jogadores = input('\nQuantos jogadores nessa partida?\n   ')
            if not quantia_jogadores.isdigit():
                print("Por favor, digite um número inteiro válido.")
            else:
                quantia_jogadores = int(quantia_jogadores)  
                if quantia_jogadores < 2:
                    print('\nPrecisa de 2 ou mais jogadores')
                elif quantia_jogadores > 10:
                    print('\nMáximo de 10 jogadores')
                else:
                    break
        print('')
        jogadores = []
        for a in range(1, quantia_jogadores + 1):
            nome = input(f'Nome do jogador {a}: ')
            jogador = {'nome': nome, 'pontos': []}
            jogadores.append(jogador)
        return jogadores
    
    def definir_dados():  # Tubo original com os 13 dados
        dados = [
            'verde', 'verde', 'verde', 'verde', 'verde', 'verde',
            'amarelo', 'amarelo', 'amarelo', 'amarelo', 
            'vermelho', 'vermelho', 'vermelho']
        return dados

    def definir_faces():  # Faces conforme as cores dos dados
        faces = {
            'verde': ['cerebro', 'cerebro', 'cerebro', 'passos', 'passos', 'tiro'],
            'amarelo': ['cerebro', 'cerebro', 'passos', 'passos', 'tiro', 'tiro'],
            'vermelho': ['cerebro', 'passos', 'passos', 'tiro', 'tiro', 'tiro']
        }
        return faces
