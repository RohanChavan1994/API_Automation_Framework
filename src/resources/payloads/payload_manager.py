from faker import Faker

faker = Faker()


def create_booking_payload():
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


def create_booking_payload_dynamic():
    payload = {
      "firstname": faker.first_name(),
      "lastname": faker.last_name(),
      "totalprice": faker.random_int(min=100, max=1000),
      "depositpaid": faker.boolean(),
      "bookingdates": {
        "checkin": str(faker.date_between(start_date='-2y', end_date='today')),
        "checkout": str(faker.date_between(start_date='today', end_date='+2y'))
      },
      "additionalneeds": faker.random_element(elements=("Breakfast", "Lunch", "Dinner"))
    }

    return payload