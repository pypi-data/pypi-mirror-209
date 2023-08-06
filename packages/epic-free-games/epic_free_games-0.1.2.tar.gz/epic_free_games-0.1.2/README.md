# Epic Free Games

![logo.png](logo.png)

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
