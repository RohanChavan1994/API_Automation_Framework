import requests
import json
import pytest
from jsonschema import validate
from src.constants.api_constants import token_url, create_get_all_bookings, update_delete_get_single_booking
from src.constants.api_constants import payload_path, schema_path


class Test_full_crud:
    def get_single_booking_after_delete_get(self, booking_id):
        url = update_delete_get_single_booking(booking_id)
        headers = {"Content-Type": "application/json",
                   "Accept": "application/json"}

        # Send GET request
        get_response = requests.get(url=url, headers=headers)
        print(get_response.text)

        # Assertions
        # assert get_response.headers["Content-Type"].__contains__("application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + get_response.headers["Content-Type"]
        assert get_response.status_code == 404, "Request failed. Expected: 404, Actual:" + str(get_response.status_code)

    def delete_booking_delete(self, token, booking_id):
        url = update_delete_get_single_booking(booking_id)
        cookie = "token=" + str(token)
        headers = {"Content-Type": "application/json",
                   "Cookie": cookie}

        # Send DELETE request
        delete_response = requests.delete(url=url, headers=headers)
        print(delete_response.text)

        # Assertions
        # assert delete_response.headers["Content-Type"].__contains__("application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + delete_response.headers["Content-Type"]
        assert delete_response.status_code == 201, "Request failed. Expected: 201, Actual:" + str(
            delete_response.status_code)

    def full_update_booking_put(self, token, booking_id):
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

    def partial_update_booking_patch(self, token, booking_id):
        url = update_delete_get_single_booking(booking_id)
        cookie = "token=" + str(token)
        headers = {"Content-Type": "application/json",
                   "Accept": "application/json",
                   "Cookie": cookie}
        path = payload_path() + r"\partial_update_payload.json"
        with open(path) as file:
            payload = json.load(file)

            # Send PATCH request
            patch_response = requests.patch(url=url, headers=headers, json=payload)
            print(patch_response.json())

            # Assertions
            assert patch_response.headers["Content-Type"].__contains__(
                "application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + patch_response.headers[
                "Content-Type"]
            assert patch_response.status_code == 200, "Request failed. Expected: 200, Actual:" + str(patch_response.status_code)

            # JSON Schema validation
            instance = patch_response.json()
            sch_path = schema_path() + r"\get_update_booking_schema.json"
            with open(sch_path) as f:
                schema = json.load(f)
                validate(instance=instance, schema=schema), "Invalid schema"

    def create_token(self):
        url = token_url()
        headers = {"Content-Type": "application/json"}
        path = payload_path() + r"\token_payload.json"
        with open(path) as file:
            payload = json.load(file)

            # Send POST request
            post_response = requests.post(url=url, headers=headers, json=payload)
            print(post_response.json())

            # JSON Schema validation
            instance = post_response.json()
            sch_path = schema_path() + r"\token_schema.json"
            with open(sch_path) as f:
                schema = json.load(f)
                validate(instance=instance, schema=schema), "Invalid schema"

            # Send newly created token for next request
            token = post_response.json()["token"]
            return token

    def get_single_booking_get(self, booking_id):
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

    def create_booking_post(self):
        url = create_get_all_bookings()
        headers = {"Content-Type": "application/json",
                   "Accept": "application/json"}
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

            # JSON Schema validation
            instance = post_response.json()
            sch_path = schema_path() + r"\create_booking_schema.json"
            with open(sch_path) as f:
                schema = json.load(f)
                validate(instance=instance, schema=schema), "Invalid schema"

            # Send Booking ID to next request
            booking_id = post_response.json()["bookingid"]
            return booking_id

    def test_main(self):
        try:
            print("Create new booking:", end=" ")
            booking_id = str(Test_full_crud().create_booking_post())
            print("New Booking ID:", booking_id)

            print("Get booking details:", end=" ")
            Test_full_crud().get_single_booking_get(booking_id)

            print("Create new token:", end=" ")
            token = str(Test_full_crud().create_token())
            print("Token details:", token)

            print("Perform partial update:", end=" ")
            Test_full_crud().partial_update_booking_patch(token, booking_id)

            print("Perform full update:", end=" ")
            Test_full_crud().full_update_booking_put(token, booking_id)

            print("Delete booking:", end=" ")
            Test_full_crud().delete_booking_delete(token, booking_id)

            print("Check if booking is present after deleting:", end=" ")
            Test_full_crud().get_single_booking_after_delete_get(booking_id)

        except Exception as error:
            print("Error occurred:", error)
