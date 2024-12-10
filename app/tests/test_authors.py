
# tests/test_authors.py
def test_create_author(client):
    response = client.post("/authors/", json={"first_name": "John", "surname": "Doe", "date_of_birth": "1980-01-01"})
    assert response.status_code == 200
    assert response.json()["first_name"] == "John"
