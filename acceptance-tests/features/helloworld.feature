Feature: Test Hello World Service

Scenario: Hello World is available
    Given I visit /helloworld
    Then the json contains Hello:World
