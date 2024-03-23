from fastapi.testclient import TestClient
from location import app  # Replace with the actual name of your FastAPI application file

client = TestClient(app)

def test_get_existing_location():
    # Test retrieving an existing location
    response = client.get("/location/zia")
    assert response.status_code == 200
    assert response.json() == {"name": "Zia", "location": "Karachi"}

def test_get_non_existing_location():
    # Test retrieving a location that does not exist
    response = client.get("/location/nonexisting")
    assert response.status_code == 404
    assert response.json() == {"detail": "No location found for nonexisting"}

def test_get_location_case_insensitivity():
    # Test case insensitivity in location names
    response = client.get("/location/ZIA")
    assert response.status_code == 200
    assert response.json() == {"name": "Zia", "location": "Karachi"}
