def create_booking_schema():
    schema = {
        "type": "object",
        "required": [
            "bookingid",
            "booking"
        ],
        "additionalProperties": True,
        "properties": {
            "bookingid": {
                "type": "integer"
            },
            "booking": {
                "type": "object",
                "required": [
                    "firstname",
                    "lastname",
                    "totalprice",
                    "depositpaid",
                    "bookingdates",
                    "additionalneeds"
                ],
                "additionalProperties": True,
                "properties": {
                    "firstname": {
                        "type": "string"
                    },
                    "lastname": {
                        "type": "string"
                    },
                    "totalprice": {
                        "type": "integer"
                    },
                    "depositpaid": {
                        "type": "boolean"
                    },
                    "bookingdates": {
                        "type": "object",
                        "required": [
                            "checkin",
                            "checkout"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "checkin": {
                                "type": "string"
                            },
                            "checkout": {
                                "type": "string"
                            }
                        }
                    },
                    "additionalneeds": {
                        "type": "string"
                    }
                }
            }
        }
    }

    return schema


def get_update_booking_schema():
    schema = {
        "type": "object",
        "required": [
            "firstname",
            "lastname",
            "totalprice",
            "depositpaid",
            "bookingdates",
            "additionalneeds"
        ],
        "additionalProperties": True,
        "properties": {
            "firstname": {
                "type": "string"
            },
            "lastname": {
                "type": "string"
            },
            "totalprice": {
                "type": "integer"
            },
            "depositpaid": {
                "type": "boolean"
            },
            "bookingdates": {
                "type": "object",
                "required": [
                    "checkin",
                    "checkout"
                ],
                "additionalProperties": True,
                "properties": {
                    "checkin": {
                        "type": "string"
                    },
                    "checkout": {
                        "type": "string"
                    }
                }
            },
            "additionalneeds": {
                "type": "string"
            }
        }
    }

    return schema


def token_schema():
    schema = {
        "type": "object",
        "required": [
            "token"
        ],
        "additionalProperties": True,
        "properties": {
            "token": {
                "type": "string"
            }
        }
    }

    return schema
