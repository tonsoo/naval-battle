# Batalha Naval
Jogo de batalha naval desenvolvido em python utilizando Pygame e Dear PyGui

## Primeira vez rodando o projeto
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r dependencies.txt
python src/main.py --mode="<dev|build>"
```

## Commits
Para realizar commits ao projeto é preciso sempre atualizar os pacotes utilizados usando o comando:
```bash
pip freeze > dependencies.txt
```