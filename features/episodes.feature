Feature: episodes API

  Background:
    Given the Futurama API is available

  @smoke
  Scenario: GET episodes by ID
    When I request the episodes with ID 1
    Then the response status code should be 200

  @regression
  Scenario: Validate basic episodes fields
    When I request the episodes with ID 1
    Then the response should contain the fields:
    | field         | value            |
    | name          | Space Pilot 3000 |
    | number        | 1                |
    | broadcastCode | S01E01           |

  @regression
  Scenario: validate season.id
    When I request the episodes with ID 1
    Then the response should contain the fields:
    | field     | value |
    | season.id | 1     |