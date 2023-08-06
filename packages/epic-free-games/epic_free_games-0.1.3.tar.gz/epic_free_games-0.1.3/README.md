# Epic Free Games

![Logo Epic Games](https://cdn2.unrealengine.com/Diesel%2Fcollections%2Ffree-games%2FEpicGamesStore_lg-black-1200x630-3b7faa2c648f075f126343747afa1a4fb9b6e1a8.png)

# A wrapper for Epic Games Store free games

# Available resources

- [x] Get Free Games

## Installation

```bash
$ pip install epic-free-games
```

## Usage

```python
from epic_free_games import EpicGames

epic_games = EpicGames()
epic_games.get_free_games()
```

# Contribute

Clone the repository project:

```bash
$ git clone https://github.com/hudsonbrendon/epic-free-games
```

Make sure [Poetry](https://python-poetry.org/) is installed, otherwise:

```bash
$ pip install -U poetry
```

Install the dependencies:

```bash
$ poetry install
```

To run the tests:

```bash
$ pytest
```

# Dependencies

- [Python >=3.10](https://www.python.org/downloads/release/python-310/)

# License

[MIT](http://en.wikipedia.org/wiki/MIT_License)
