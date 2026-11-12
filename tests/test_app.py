import src.app as app_module
from fastapi.testclient import TestClient


def test_signup_adds_student_to_activity(monkeypatch):
    # Arrange
    participants = ["existing@mergington.edu"]
    monkeypatch.setattr(
        app_module,
        "activities",
        {"Chess Club": {"participants": participants}},
    )
    client = TestClient(app_module.app)

    # Act
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "new@mergington.edu"},
    )

    # Assert
    assert response.status_code == 200
    assert participants == [
        "existing@mergington.edu",
        "new@mergington.edu",
    ]


def test_signup_rejects_student_already_registered(monkeypatch):
    # Arrange
    participants = ["student@mergington.edu"]
    monkeypatch.setattr(
        app_module,
        "activities",
        {"Chess Club": {"participants": participants}},
    )
    client = TestClient(app_module.app)

    # Act
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": "student@mergington.edu"},
    )

    # Assert
    assert response.status_code == 400
    assert participants == ["student@mergington.edu"]
