import requests


def test_age_identifier():
    url = "https://api.agify.io?name=rohan"
    response = requests.get(url=url)
    print(response.text)
