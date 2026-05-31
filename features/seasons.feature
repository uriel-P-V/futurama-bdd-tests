Feature: season API

  Background:
    Given the Futurama API is available

  @smoke
  Scenario: GET season by ID
    When I request the season with ID 1
    Then the response status code should be 200

  @regression
  Scenario: validate that season 1 has more than 5 episodes
    When I request the season with ID 1
    Then the response should contain more than 5 episodes
    

