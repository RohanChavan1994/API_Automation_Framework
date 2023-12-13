# Common headers
def common_headers():
    headers = {"Content-Type": "application/json"}
    return headers


def common_headers_xml():
    headers = {"Content-Type": "application/xml"}
    return headers


def create_booking_headers():
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}
    return headers
