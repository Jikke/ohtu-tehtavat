from statistics import Statistics
from player_reader import PlayerReader
from matchers import QueryBuilder, And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or, All

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    """
    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )
    """
    query = QueryBuilder()
    matcher = (
  query
    .oneOf(
      query.playsIn("PHI")
          .hasAtLeast(10, "assists")
          .hasFewerThan(5, "goals")
          .build(),
      query.playsIn("EDM")
          .hasAtLeast(40, "points")
          .build()
    )
    .build()
)
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
