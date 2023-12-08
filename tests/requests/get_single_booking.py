import requests
import json
from jsonschema import validate
from src.constants.api_constants import update_delete_get_single_booking
from src.constants.api_constants import schema_path


def get_single_booking(booking_id):
    url = update_delete_get_single_booking(booking_id)
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}

    # Send GET request
    get_response = requests.get(url=url, headers=headers)
    print(get_response.json())

    # Assertions
    assert get_response.headers["Content-Type"].__contains__(
        "application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + get_response.headers[
        "Content-Type"]
    assert get_response.status_code == 200, "Request failed. Expected: 200, Actual:" + str(get_response.status_code)

    # JSON Schema validation
    instance = get_response.json()
    sch_path = schema_path() + r"\get_update_booking_schema.json"
    with open(sch_path) as f:
        schema = json.load(f)
        validate(instance=instance, schema=schema), "Invalid schema"
