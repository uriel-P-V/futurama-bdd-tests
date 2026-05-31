from behave import when
import requests

API_BASE_URL = "https://futuramaapi.com/api"

@when("I request the episodes with ID {episodes_id:d}")
def step_when_request_crew(context, episodes_id):
    context.response = requests.get(
        f"{API_BASE_URL}/episodes/{episodes_id}"
    )