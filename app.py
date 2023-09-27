from src.controller.controller import Jogo

Jogo.apresenta()

jogadores = Jogo.define_jogadores()
tubo_dados = Jogo.define_tubo_dados()



# Testes
print(tubo_dados[0])
for chave, valor in tubo_dados[1].items():
    print(f"{chave}: {valor}")
