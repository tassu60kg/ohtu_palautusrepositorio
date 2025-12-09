from statistics import Statistics
from player_reader import PlayerReader
from matchers import Not, And, HasAtLeast, PlaysIn, HasFewerThan, All, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    #matcher = And(
        #Not(HasAtLeast(2, "goals")),
        #HasFewerThan(2, "goals"),
        #PlaysIn("NYR")
        #HasAtLeast(5, "goals"),
        #HasAtLeast(20, "assists"),
      #  PlaysIn("PHI"),
     #   Not(HasAtLeast(2,"goals"))
    #)
    matcher = And(
    HasAtLeast(70, "points"),
    Or(
        PlaysIn("COL"),
        PlaysIn("FLA"),
        PlaysIn("BOS")
    )
    )


    for player in stats.matches(matcher):
        print(player)

    print(len(stats.matches(All())))
if __name__ == "__main__":
    main()
