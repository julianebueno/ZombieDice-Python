class Modelos():

    def coletar_jogadores():
        while True:
            quantia_jogadores = input('\nQuantos jogadores nessa partida?\n   ')
            if not quantia_jogadores.isdigit():
                print("Por favor, digite um número inteiro válido.")
            else:
                quantia_jogadores = int(quantia_jogadores)  
                if quantia_jogadores < 2:
                    print('')
                    print('Precisa de 2 ou mais jogadores')
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
            '⬜', '⬜', '⬜', '⬜', '⬜', '⬜',
            '🟨', '🟨', '🟨', '🟨', 
            '🟦', '🟦', '🟦']
        return dados

    def definir_faces():  # Faces conforme as cores dos dados
        faces = {
            '⬜': ['🧠', '🧠', '🧠', '👣', '👣', '🔫'],
            '🟨': ['🧠', '🧠', '👣', '👣', '🔫', '🔫'],
            '🟦': ['🧠', '👣', '👣', '🔫', '🔫', '🔫']
        }
        return faces
