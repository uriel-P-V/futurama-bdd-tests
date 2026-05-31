from behave import when
import requests

API_BASE_URL = "https://futuramaapi.com/api"

@when("I request the season with ID {season_id:d}")
def step_when_request_fruit(context, season_id):
    context.response = requests.get(
        f"{API_BASE_URL}/seasons/{season_id}"
    )
    
@then("the response should contain more than 5 episodes")
def step_then_more_than_5_episodes(context):
    data = context.response.json()
    assert len(data["episodes"]) > 5, (
        f"Expected more than 5 episodes but got {len(data['episodes'])}"
    )