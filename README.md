# Game of Life (Jogo da Vida)

## Histórico
Foi criado a fim de reproduzir as alterações e mudanças em grupos de seres vivos.
As regras definidas são aplicadas a cada nova "geração".

## Regras do jogo
1. Toda célula morta com exatamente três vizinhos vivos torna-se viva (nascimento).

2. Toda célula viva com menos de dois vizinhos vivos morre por isolamento.

3. Toda célula viva com mais de três vizinhos vivos morre por superpopulação.

4. Toda célula viva com dois ou três vizinhos vivos permanece viva

![Rules of Game](/Img/rules.png "Rules of Game")

>
 
Antes de testar o jogo, rode os comandos abaixo(cria um ambiente virtual e instala as dependências do projeto):
```
virtualenv .venv
source .venv/bin/activate
pip install requirements.txt

```

## Rodar em Python
```
cd Python
python3 game_of_life.py

```

## Rodar em Vue



