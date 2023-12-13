import requests
import json
from jsonschema import validate
from src.constants.api_constants import create_get_all_bookings
from src.constants.api_constants import payload_path, schema_path
from src.helpers.utils import create_booking_headers


def test_create_booking():
    url = create_get_all_bookings()
    headers = create_booking_headers()
    path = payload_path() + r"\create_booking_payload.json"

    with open(path) as file:
        payload = json.load(file)

        # Send POST request
        post_response = requests.post(url=url, headers=headers, json=payload)
        print(post_response.json())

        # Assertions
        assert post_response.headers["Content-Type"].__contains__(
            "application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + post_response.headers[
            "Content-Type"]
        assert post_response.status_code == 200, "Request failed. Expected: 200, Actual:" + str(post_response.status_code)
        assert post_response.elapsed.total_seconds() < 2, "Time taken more has 3 seconds. Actual time taken:" + str(post_response.elapsed.total_seconds())

        # JSON Schema validation
        instance = post_response.json()
        sch_path = schema_path() + r"\create_booking_schema.json"
        with open(sch_path) as f:
            schema = json.load(f)
            validate(instance=instance, schema=schema), "Invalid schema"

        # Send Booking ID to next request
        booking_id = post_response.json()["bookingid"]
        return booking_id
