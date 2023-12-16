# Read the CSV or Excel file
# Create a function create_token which can take the values from Excel file
# Verify the expected results

import openpyxl
import requests
import pytest
from src.constants.api_constants import *
from src.helpers.utils import *


# Step 1: Read the file and put the contents in a []
def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    return credentials


def make_request_auth(username, password):
    url = token_url()
    headers = create_booking_headers()
    payload = {
        "username": username,
        "password": password
    }
    response = requests.post(url=url, headers=headers, json=payload)
    print(response.json())
    return response


@pytest.mark.parametrize("user_cred", read_credentials_from_excel(r"C:\Users\Lenovo\PycharmProjects\API_Automation_Framework\tests\datadriventesting\testdata.xlsx"))
def test_post_create_token(user_cred):
    username = user_cred["username"]
    password = user_cred["password"]
    print(username, password)
    response = make_request_auth(username, password)
    print(response)
