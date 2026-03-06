def test_get_activities_returns_dictionary(client):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload


def test_get_activities_contains_expected_fields(client):
    # Arrange
    url = "/activities"

    # Act
    response = client.get(url)
    payload = response.json()
    chess_club = payload["Chess Club"]

    # Assert
    assert response.status_code == 200
    assert "description" in chess_club
    assert "schedule" in chess_club
    assert "max_participants" in chess_club
    assert "participants" in chess_club
    assert isinstance(chess_club["participants"], list)
