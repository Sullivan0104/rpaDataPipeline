from src.fetch_swapi import fetch_data

def test_fetch_people():
    data = fetch_data("people")
    assert "results" in data
    assert len(data["results"]) > 0
