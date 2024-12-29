# 🎲 Zombie Dice 🎲
[![Python 3.10.4](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3104/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### Índice
- [Como jogar](#como-jogar)
- [Instalação](#instalação)
- [Screenshots](#)

## Como jogar

Para jogar é preciso pelo menos dois jogadores. Eles serão os zumbis em busca de cérebros 🧟

Cada dado representa uma pobre vítima a ser atacada

O jogo tem 13 dados, cada um tem uma cor, cada cor tem uma configuração de faces, sendo:

- 6 verde: 3 cerebro, 2 passos e 1 tiro
- 4 amarelo: 2 cerebro, 2 passos e 2 tiro
- 3 vermelho: 1 cerebro, 2 passos e 3 tiro

As faces significam:
- cerebro – Você devorou o cérebro de sua vítima. Ganha ponto e o dado fica preso durante o turno do jogador
- passos – Sua vítima escapou. Sempre retorna para ser jogado novamente
- tiro – Sua vítima revidou. Se juntar 3 no turno, perde a vez ☠️

Em cada rodada, 3 dados são sortidos e rolados, e o resultado é computado e o jogador escolhe em continuar ou passar a vez

Jogue até alguém chegar a 13 Cérebros 🏆

## Instalação

Baixe e instale o [Python](https://www.python.org/downloads/)

Clone o projeto no terminal com o [git](https://git-scm.com/) (ou [baixe em .zip](https://github.com/julianebueno/ZombieDice-Python/archive/refs/heads/main.zip), descompacte e abra no terminal)
```
git clone https://github.com/julianebueno/ZombieDice-Python.git
```

Entre na pasta do Jogo
```
cd ZombieDice-Python
```

Rode o Jogo
```
python ./app.py
```

## Screenshots

- Início

![alt text](/src/img/image1.png)

- Passa a vez

![alt text](/src/img/image2.png)

- Soma dos pontos

![alt text](/src/img/image3.png)

- Perda da rodada por tiro

![alt text](/src/img/image4.png)

- Final com o vencedor

![alt text](/src/img/image5.png)

---
Feito por Juliane Bueno
