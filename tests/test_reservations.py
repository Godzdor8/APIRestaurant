import datetime

def test_create_reservation(client):
    # Сначала создаём столик
    table_resp = client.post("/tables/", json={
        "name": "Table for Reservation",
        "seats": 4,
        "location": "Main"
    })
    table_id = table_resp.json()["id"]

    reservation_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).isoformat()

    response = client.post("/reservations/", json={
        "customer_name": "John Doe",
        "table_id": table_id,
        "reservation_time": reservation_time,
        "duration_minutes": 60
    })

    assert response.status_code == 200
    assert response.json()["customer_name"] == "John Doe"

def test_conflicting_reservation(client):
    # Используем тот же столик и время, что и в предыдущем тесте
    table_id = client.get("/tables/").json()[-1]["id"]
    reservation_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=1)).isoformat()

    response = client.post("/reservations/", json={
        "customer_name": "Conflict Test",
        "table_id": table_id,
        "reservation_time": reservation_time,
        "duration_minutes": 60
    })

    assert response.status_code == 400
    assert "уже забронирован" in response.json()["detail"]

def test_delete_reservation(client):
    reservations = client.get("/reservations/").json()
    if reservations:
        reservation_id = reservations[0]["id"]
        response = client.delete(f"/reservations/{reservation_id}")
        assert response.status_code == 200