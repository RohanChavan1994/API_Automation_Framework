import requests
import json
from jsonschema import validate
from src.constants.api_constants import token_url
from src.constants.api_constants import payload_path, schema_path


def create_token():
    url = token_url()
    headers = {"Content-Type": "application/json"}
    path = payload_path() + r"\token_payload.json"
    with open(path) as file:
        payload = json.load(file)

        # Send POST request
        post_response = requests.post(url=url, headers=headers, json=payload)
        print(post_response.json())

        # JSON Schema validation
        instance = post_response.json()
        sch_path = schema_path() + r"\token_schema.json"
        with open(sch_path) as f:
            schema = json.load(f)
            validate(instance=instance, schema=schema), "Invalid schema"

        # Send newly created token for next request
        token = post_response.json()["token"]
        return token
