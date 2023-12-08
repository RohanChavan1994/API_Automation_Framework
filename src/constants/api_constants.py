# Add your constants here

def base_url():
    return "https://restful-booker.herokuapp.com"


def token_url():
    return "https://restful-booker.herokuapp.com/auth"


def create_get_all_bookings():
    return "https://restful-booker.herokuapp.com/booking"


def update_delete_get_single_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)


def ping_healthcheck():
    return "https://restful-booker.herokuapp.com/ping"


def payload_path():
    return r"C:\Users\Lenovo\PycharmProjects\API_Automation_Framework\src\resources\payloads"


def schema_path():
    return r"C:\Users\Lenovo\PycharmProjects\API_Automation_Framework\src\resources\schemas"