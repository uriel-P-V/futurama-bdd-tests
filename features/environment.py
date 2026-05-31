from unittest.mock import patch, MagicMock

API_BASE_URL = "https://futuramaapi.com/api"


MOCK_CHARACTER = {
    "id": 1,
    "name": "Philip J. Fry",
    "gender": "MALE",
    "status": "ALIVE",
    "species": "HUMAN"
}

MOCK_EPISODE = {
    "id": 1,
    "name": "Space Pilot 3000",
    "number": 1,
    "broadcastCode": "S01E01",
    "season": {"id": 1}
}

MOCK_SEASON = {
    "id": 1,
    "episodes": [{"id": i} for i in range(1, 10)]
}

MOCK_ERROR = {
    "detail": "Character not found"
}


def unified_mock_get(url, **kwargs):
    mock = MagicMock()

    if url == f"{API_BASE_URL}/characters/1":
        mock.status_code = 200
        mock.json.return_value = MOCK_CHARACTER

    elif url == f"{API_BASE_URL}/seasons/1":
        mock.status_code = 200
        mock.json.return_value = MOCK_SEASON
    
    elif url == f"{API_BASE_URL}/episodes/1":
        mock.status_code = 200
        mock.json.return_value = MOCK_EPISODE

    elif url == f"{API_BASE_URL}/characters/9999":
        mock.status_code = 404
        mock.json.return_value = MOCK_ERROR

    return mock


def before_scenario(context, scenario):
    print(f"Starting scenario: {scenario.name}")

    if "regression" in scenario.tags:
        context.mock_get = patch("requests.get", side_effect=unified_mock_get)
        context.mock_get.start()


def after_scenario(context, scenario):
    print( f"Finished scenario: " f"{scenario.name} - Status: {scenario.status}")

    if "regression" in scenario.tags:
        context.mock_get.stop()