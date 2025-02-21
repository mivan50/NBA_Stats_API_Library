from basketball_stats.player import Player


def test_get_season_stats():
    player = Player("LeBron", "James")
    season_stats = player.get_season_stats(2020)
    assert season_stats is not None, "Season stats for 2020 should not be None"
    print(f"Season Stats for 2020: {season_stats}")


def test_get_career_stats():
    player = Player("LeBron", "James")
    career_stats = player.get_career_stats()
    assert career_stats is not None, "Career stats should not be None"
    print(f"Career Stats: {career_stats}")


if __name__ == "__main__":
    test_get_season_stats()
    test_get_career_stats()
