Feature: characters API

  Background:
    Given the Futurama API is available

  @smoke
  Scenario: GET Fry by ID
    When I request the Fry with ID 1
    Then the response status code should be 200

  @regression
  Scenario: Validate basic Fry fields
    When I request the Fry with ID 1
    Then the response should contain the fields:
      | field  | value         |
      | name   | Philip J. Fry |
      | gender | MALE          |
      | status | ALIVE         |
      | species| HUMAN         |

  @regression
  Scenario: invalid character
    When I request the Fry with ID 9999
    Then the response status code should be 404
    And the error message should be "Character not found"