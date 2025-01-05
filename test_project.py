import pytest
from project import add_to_watchlist, mark_as_watched, load_watchlist

# Test add_to_watchlist function
def test_add_to_watchlist():
    watchlist = ["Inception", "Titanic"]
    add_to_watchlist("Avatar", watchlist)
    assert "Avatar" in watchlist

    add_to_watchlist("Inception", watchlist)
    assert watchlist.count("Inception") == 1  # No duplicates allowed

# Test mark_as_watched function
def test_mark_as_watched():
    watchlist = ["Inception", "Titanic"]
    mark_as_watched("Inception", watchlist)
    assert "Inception" not in watchlist

    mark_as_watched("Avatar", watchlist)
    assert "Avatar" not in watchlist  # Should not affect the list if the movie isn't there

# Test load_watchlist function
def test_load_watchlist(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    file = d / "films.csv"
    file.write_text("Inception\nTitanic\n")

    watchlist = load_watchlist(file)
    assert watchlist == ["Inception", "Titanic"]
