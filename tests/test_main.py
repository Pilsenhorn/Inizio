from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch

client = TestClient(app)

def fake_get_google_results(query: str):
    return [
        {
            "title": "Test title",
            "link": "https://test.com",
            "snippet": "Test snippet"
        }
    ]
@patch("main.get_google_results", side_effect=fake_get_google_results)
def test_search(mock_func):
    response = client.get("/search?q=test")
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert isinstance(data["results"], list)
    item = data["results"][0]
    assert "title" in item
    assert "link" in item
    assert "snippet" in item