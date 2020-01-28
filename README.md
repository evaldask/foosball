# foosball

Computes foosball ratings for each individual player using [TrueSkill](https://trueskill.org/) metric. Supports 2 vs 2, 1 vs 1 or 2 vs 1 matches.

To run it, just use `python compute.py`. Python 3.6 and up.

Dependencies:
```
- pandas
- trueskill
```

To install them, choose one below:
- `pip install pandas trueskill`
- `poetry add pandas trueskill`
- or if cloned the repo: `poetry install`



## Data
`compute.py` reads a CSV file from `data/` folder called `games.csv`. It structured like this:
```
Date,Player#1_1,Player#1_2,Score1,Score2,Player#2_1,Player#2_2
```

Where:
```
Date - when the game happened

Player#1_1 - first player from team #1
Player#1_2 - second player from team #1

Score1 - how many games team #1 won or how many goals team #1 scored
Score2 - how many games team #2 won or how many goals team #2 scored

Player#2_1 - first player from team #2
Player#2_2 - second player from team #2
```
The script produces an output CSV in `data/results.csv`.
The structure of this file:
```
Name,Mu,Sigma
```

Where:
```
Name - player's name
Mu - skill value (higher -> better)
Sigma - uncertainty about the skill (lower -> better)
```
