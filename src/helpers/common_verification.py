# HTTP Status COde verification

def verify_http_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Request failed. Expected: 200, Actual:" + str(response_data.status_code)


def verify_json_key_for_not_null(key):
    assert key != 0, "Key is empty" + key
    assert key > 0, "Key is empty" + key


def verify_response(key):
    assert key is not None


def verify_response_time(key):
    pass
