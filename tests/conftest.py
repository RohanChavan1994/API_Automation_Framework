import requests
import json
import pytest
from jsonschema import validate
from src.constants.api_constants import token_url, create_get_all_bookings, update_delete_get_single_booking
from src.resources.payloads.payload_manager import *
from src.resources.schemas.schema_manager import *


@pytest.fixture()
def create_booking_post():
    url = create_get_all_bookings()
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}
    payload = create_booking_payload()
	#=====================
    # Send POST request
    post_response = requests.post(url=url, headers=headers, json=payload)
    print(post_response.json())

    # Assertions
    assert post_response.headers["Content-Type"].__contains__(
        "application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + \
                             post_response.headers[
                                 "Content-Type"]
    assert post_response.status_code == 200, "Request failed. Expected: 200, Actual:" + str(
        post_response.status_code)

    # JSON Schema validation
    instance = post_response.json()
    schema = create_booking_schema()
    validate(instance=instance, schema=schema), "Invalid schema"

    # Send Booking ID to next request
    booking_id = post_response.json()["bookingid"]
    return booking_id


@pytest.fixture()
def get_single_booking_get(create_booking_post):
    booking_id = create_booking_post
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
    schema = get_update_booking_schema()
    validate(instance=instance, schema=schema), "Invalid schema"

    return booking_id


@pytest.fixture()
def create_token():
    url = token_url()
    headers = {"Content-Type": "application/json"}
    payload = token_payload()

    # Send POST request
    post_response = requests.post(url=url, headers=headers, json=payload)
    print(post_response.json())

    # JSON Schema validation
    instance = post_response.json()
    schema = token_schema()
    validate(instance=instance, schema=schema), "Invalid schema"

    # Send newly created token for next request
    token = post_response.json()["token"]
    return token


@pytest.fixture()
def partial_update_booking_patch(create_token, create_booking_post):
    token = create_token
    booking_id = create_booking_post
    url = update_delete_get_single_booking(booking_id)
    cookie = "token=" + str(token)
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Cookie": cookie}
    payload = partial_update_payload()

    # Send PATCH request
    patch_response = requests.patch(url=url, headers=headers, json=payload)
    print(patch_response.json())

    # Assertions
    assert patch_response.headers["Content-Type"].__contains__(
        "application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + \
                             patch_response.headers[
                                 "Content-Type"]
    assert patch_response.status_code == 200, "Request failed. Expected: 200, Actual:" + str(
        patch_response.status_code)

    # JSON Schema validation
    instance = patch_response.json()
    schema = get_update_booking_schema()
    validate(instance=instance, schema=schema), "Invalid schema"


@pytest.fixture()
def full_update_booking_put(create_token, create_booking_post):
    token = create_token
    booking_id = create_booking_post
    url = update_delete_get_single_booking(booking_id)
    cookie = "token=" + str(token)
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Cookie": cookie}
    payload = full_update_payload()

    # Send PUT request
    put_response = requests.put(url=url, headers=headers, json=payload)
    print(put_response.json())

    # Assertions
    assert put_response.headers["Content-Type"].__contains__(
        "application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + put_response.headers[
        "Content-Type"]
    assert put_response.status_code == 200, "Request failed. Expected: 200, Actual:" + str(
        put_response.status_code)

    # JSON Schema validation
    instance = put_response.json()
    schema = get_update_booking_schema()
    validate(instance=instance, schema=schema), "Invalid schema"


@pytest.fixture()
def delete_booking_delete(create_token, create_booking_post):
    token = create_token
    booking_id = create_booking_post
    url = update_delete_get_single_booking(booking_id)
    cookie = "token=" + str(token)
    headers = {"Content-Type": "application/json",
               "Cookie": cookie}

    # Send DELETE request
    delete_response = requests.delete(url=url, headers=headers)
    print(delete_response.text)

    # Assertions
    assert delete_response.status_code == 201, "Request failed. Expected: 201, Actual:" + str(
        delete_response.status_code)

    return booking_id


@pytest.fixture()
def get_single_booking_after_delete_get(delete_booking_delete):
    booking_id = delete_booking_delete
    url = update_delete_get_single_booking(booking_id)
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}

    # Send GET request
    get_response = requests.get(url=url, headers=headers)
    print(get_response.text)

    # Assertions
    # assert get_response.headers["Content-Type"].__contains__("application/json"), "Invalid Content-Type. Expected: application/json, Actual:" + get_response.headers["Content-Type"]
    assert get_response.status_code == 404, "Request failed. Expected: 404, Actual:" + str(get_response.status_code)
