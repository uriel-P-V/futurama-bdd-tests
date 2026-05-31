from behave import when
import requests

API_BASE_URL = "https://futuramaapi.com/api"


@when("I request the Fry with ID {character_id:d}")
def step_when_request_character(context, character_id):
    context.response = requests.get(
        f"{API_BASE_URL}/characters/{character_id}"
    )