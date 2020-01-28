from collections import defaultdict
import pandas as pd
import trueskill as ts

from typing import Iterable, Tuple


DATE_COLUMN = "Date"


def compute_rank(score1: float, score2: float) -> Tuple[float, float]:
    # Lower rank is better.
    if score1 > score2:
        return [0, 1]

    if score1 < score2:
        return [1, 0]

    return [0, 0]


def append(
    name: str, players: dict, team: Iterable[str], skills: Iterable[ts.Rating]
) -> Tuple[Iterable[str], Iterable[ts.Rating]]:
    if name is not None and name != "":
        return team + [name], skills + [players[name]]

    return team, skills


def update(players: dict, team: Iterable[str], ratings: Iterable[ts.Rating]):
    for name, rating in zip(team, ratings):
        players[name] = rating


def main(games_file: str, ratings_file: str):
    # Load data.
    players = defaultdict(lambda: ts.Rating())
    games = pd.read_csv(games_file)

    # Sort data based on date.
    games.sort_values(by=[DATE_COLUMN], inplace=True)
    games.fillna("", inplace=True)

    for _, (date, pl1, pl2, sc1, sc2, pl3, pl4) in games.iterrows():
        team1 = []
        skills1 = []

        team2 = []
        skills2 = []

        team1, skills1 = append(pl1, players, team1, skills1)
        team1, skills1 = append(pl2, players, team1, skills1)

        team2, skills2 = append(pl3, players, team2, skills2)
        team2, skills2 = append(pl4, players, team2, skills2)

        ranks = compute_rank(sc1, sc2)

        ratings1, ratings2 = ts.rate([skills1, skills2], ranks=ranks)
        update(players, team1, ratings1)
        update(players, team2, ratings2)


    # Save ratings.
    result = []
    for name, rating in players.items():
        result.append({"Name": name, "Mu": rating.mu, "Sigma": rating.sigma})

    df = pd.DataFrame(result)
    df.to_csv(ratings_file, index=False)


if __name__ == "__main__":
    main("data/games.csv", "data/results.csv")
