def payload_create_booking():
    payload = {
      "firstname": "James",
      "lastname": "Bond",
      "totalprice": 250,
      "depositpaid": True,
      "bookingdates": {
        "checkin": "2023-12-22",
        "checkout": "2023-12-27"
      },
      "additionalneeds": "Breakfast"
    }

    return payload
