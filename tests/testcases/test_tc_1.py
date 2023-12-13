from src.resources.requests.create_booking import create_booking
from src.resources.requests.get_single_booking import get_single_booking
from src.resources.requests.create_token import create_token
from src.resources.requests.partial_update import partial_update
from src.resources.requests.full_update import full_update
from src.resources.requests.delete_booking import delete_booking


class Test_tc1:
    def test_main(self):
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
