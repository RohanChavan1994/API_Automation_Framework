from tests.requests.create_booking import create_booking
from tests.requests.get_single_booking import get_single_booking
from tests.requests.create_token import create_token
from tests.requests.partial_update import partial_update
from tests.requests.full_update import full_update
from tests.requests.delete_booking import delete_booking


def test_main():
    try:
        print("Create new booking:", end=" ")
        booking_id = str(create_booking())
        print("New Booking ID:", booking_id)

        print("Get booking details:", end=" ")
        get_single_booking(booking_id)

        print("Create new token:", end=" ")
        token = str(create_token())
        print("Token details:", token)

        print("Perform partial update:", end=" ")
        partial_update(token, booking_id)

        print("Perform full update:", end=" ")
        full_update(token, booking_id)

        print("Delete booking:", end=" ")
        delete_booking(token, booking_id)

        # print("Check if booking is present after deleting:", end=" ")
        # get_single_booking_after_delete_get(booking_id)

    except Exception as error:
        print("Error occurred:", error)
