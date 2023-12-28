
from tests.conftest import *


def test_create_booking_post(create_booking_post):
    create_booking_post


def test_get_single_booking_get(get_single_booking_get):
    get_single_booking_get


def test_create_token(create_token):
    create_token


def test_partial_update_booking_patch(partial_update_booking_patch):
    partial_update_booking_patch


def test_full_update_booking_put(full_update_booking_put1):
    full_update_booking_put1


def test_delete_booking_delete(delete_booking_delete):
    delete_booking_delete


def test_get_single_booking_after_delete_get(get_single_booking_after_delete_get):
    get_single_booking_after_delete_get
