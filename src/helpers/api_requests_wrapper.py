# To make POST, PUT, PATCH, DELETE
# HTTP Methods - Generic Functions

import requests


def get_request_in_json(url, auth, in_json):
    response = requests.get(url=url, auth=auth)

    if in_json is True:
        return response.json()
    else:
        return response


def post_request_in_json(url, headers, payload, auth, in_json):
    response = requests.post(url=url, headers=headers, json=payload, auth=auth)

    if in_json is True:
        return response.json()
    else:
        return response


def put_request_in_json(url, headers, payload, auth, in_json):
    response = requests.put(url=url, headers=headers, json=payload, auth=auth)

    if in_json is True:
        return response.json()
    else:
        return response


def patch_request_in_json(url, headers, payload, auth, in_json):
    response = requests.patch(url=url, headers=headers, json=payload, auth=auth)

    if in_json is True:
        return response.json()
    else:
        return response


def delete_request_in_json(url, headers, auth, in_json):
    response = requests.delete(url=url, headers=headers, auth=auth)

    if in_json is True:
        return response.json()
    else:
        return response
