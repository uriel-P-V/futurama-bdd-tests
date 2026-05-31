# futurama-bdd-tests

![CI](https://github.com/uriel-P-V/futurama-bdd-tests/actions/workflows/tests.yml/badge.svg)

A BDD-based test suite for the Futurama API —
demonstrates multi-feature Gherkin organization with characters, episodes and seasons,
including dot-notation for nested season objects, structured error validation,
and episode count validation.

---

## Project Structure

```
futurama-bdd-tests/
├── .github/
│   └── workflows/
│       └── tests.yml                  ← GitHub Actions CI
├── features/
│   ├── steps/
│   │   ├── common_steps.py            ← Shared steps across features
│   │   ├── characters_steps.py        ← Character GET step
│   │   ├── episodes_steps.py          ← Episode GET step
│   │   └── seasons_steps.py           ← Season GET and episode count step
│   ├── environment.py                 ← Hooks and unified mock
│   ├── characters.feature             ← Fry fields and 404 error validation
│   ├── episodes.feature               ← Episode fields and season.id dot-notation
│   └── seasons.feature                ← Season episode count validation
└── requirements.txt
```

---

## Features

- **Structured error validation** — verifies `detail` field on 404 responses
- **Dot-notation** — `season.id` nested field access
- **Episode count validation** — verifies season has more than 5 episodes
- **Real 404 support** — API correctly returns 404 for invalid IDs
- **Single mock** — one `patch("requests.get")` dispatching by URL
- **Tag-driven execution** — `@smoke` hits real API, `@regression` fully mocked
- **GitHub Actions CI** — smoke runs first, regression only if smoke passes

---

## BDD Scenarios

```gherkin
Feature: characters API

  @regression
  Scenario: invalid character
    When I request the Fry with ID 9999
    Then the response status code should be 404
    And the error message should be "Character not found"

Feature: episodes API

  @regression
  Scenario: validate season.id
    When I request the episodes with ID 1
    Then the response should contain the fields:
      | field     | value |
      | season.id | 1     |

Feature: season API

  @regression
  Scenario: validate that season 1 has more than 5 episodes
    When I request the season with ID 1
    Then the response should contain more than 5 episodes
```

---

## Mock Strategy

Single `patch("requests.get")` dispatching by URL:

```python
def unified_mock_get(url, **kwargs):
    if url == f"{API_BASE_URL}/characters/1":
        mock.json.return_value = MOCK_CHARACTER
    elif url == f"{API_BASE_URL}/characters/9999":
        mock.status_code = 404
        mock.json.return_value = {"detail": "Character not found"}
    elif url == f"{API_BASE_URL}/episodes/1":
        mock.json.return_value = MOCK_EPISODE
    elif url == f"{API_BASE_URL}/seasons/1":
        mock.json.return_value = MOCK_SEASON
```

---

## Setup

```bash
git clone https://github.com/uriel-P-V/futurama-bdd-tests.git
cd futurama-bdd-tests
pip install -r requirements.txt
behave
```

---

## Running Tests

```bash
# All scenarios
behave

# Smoke only — hits real Futurama API
behave --tags=smoke

# Regression only — fully mocked, no internet required
behave --tags=regression
```

---

## CI/CD Pipeline

Two dependent jobs run on every push and pull request to `main`:

```
push / PR → smoke (3 scenarios) → regression (5 scenarios)
```

If `smoke` fails, `regression` is skipped automatically.

---

## Tech Stack

- **Python 3.11+**
- **Behave** — BDD framework with Gherkin support
- **Requests** — HTTP client for API calls
- **unittest.mock** — patch, MagicMock, side_effect
- **GitHub Actions** — CI/CD pipeline

---

## Author

**Uriel Alejandro Pérez Valdovinos**  
[github.com/uriel-P-V](https://github.com/uriel-P-V) · [linkedin.com/in/uriel-pv](https://linkedin.com/in/uriel-pv)