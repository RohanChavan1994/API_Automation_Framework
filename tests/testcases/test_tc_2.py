import json

import pytest
import requests

from src.constants.api_constants import create_get_all_bookings, payload_path, schema_path
from jsonschema import validate


class Testcase_2:
    def test_1(self):
        url = create_get_all_bookings()

        headers = {"Content-Type": "application/json",
                   "Accept": "application/json"}
        path = payload_path() + r"\create_booking_payload.json"
        with open(path) as f:
            payload = json.load(f)
            post_response = requests.post(url=url, headers=headers, json=payload)
            print(post_response.json())
            print(post_response.elapsed.total_seconds())

            # Assertions
            assert post_response.status_code == 200, "Expected: 200, Actual:" + str(post_response.status_code)
            assert post_response.elapsed.total_seconds() < 2, "Expected less than 500 ms, Actual time taken:" + str(
                post_response.elapsed.total_seconds())

            sch_path = schema_path() + r"\create_booking_schema.json"
            with open(sch_path) as h:
                schema = json.load(h)
                validate(instance=post_response.json(), schema=schema), "Invalid schema"
