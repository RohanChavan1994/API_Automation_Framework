import json
import requests
from jsonschema import validate
from src.constants.api_constants import payload_path, schema_path
from src.constants.api_constants import update_delete_get_single_booking


def full_update(token, booking_id):
    url = update_delete_get_single_booking(booking_id)
    cookie = "token=" + str(token)
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Cookie": cookie}
    path = payload_path() + r"\full_update_payload.json"
    with open(path) as file:
        payload = json.load(file)

        # Send PUT request
        put_response = requests.put(url=url, headers=headers, json=payload)
        print(put_response.json())

        # Assertions
        assert put_response.headers["Content-Type"].__contains__(
            "application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + put_response.headers[
            "Content-Type"]
        assert put_response.status_code == 200, "Request failed. Expected: 200, Actual:" + str(put_response.status_code)

        # JSON Schema validation
        instance = put_response.json()
        sch_path = schema_path() + r"\get_update_booking_schema.json"
        with open(sch_path) as f:
            schema = json.load(f)
            validate(instance=instance, schema=schema), "Invalid schema"
