import requests
from src.constants.api_constants import update_delete_get_single_booking


def delete_booking(token, booking_id):
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
