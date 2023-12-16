import json

import pytest
import requests

from src.constants.api_constants import create_get_all_bookings
from jsonschema import validate
from src.resources.payloads.payload_manager import *
from src.resources.schemas.schema_manager import *
from src.helpers.utils import *


class Testcase_4:
    def test_1(self):
        url = create_get_all_bookings()
        headers = create_booking_headers()
        payload = create_booking_payload_dynamic()

        post_response = requests.post(url=url, headers=headers, json=payload)
        print(post_response.json())
        print(post_response.elapsed.total_seconds())

        # Assertions
        assert post_response.status_code == 200, "Expected: 200, Actual:" + str(post_response.status_code)
        assert post_response.elapsed.total_seconds() < 3, "Expected less than 500 ms, Actual time taken:" + str(post_response.elapsed.total_seconds())

        schema = create_booking_schema()
        validate(instance=post_response.json(), schema=schema), "Invalid schema"
