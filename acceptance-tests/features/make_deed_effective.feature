@make_deed_effective

Feature: Make Deed Effective
    As a Conveyancer I want to be able to make a deed effective
    So that it is ready for submission to Land Registry

Background:
    Given I make a deed effective

Scenario: Date and Signature Applied when Deed is Made Effective

    - Date must be added to the deed which consists of time stamp (current datetime)
    - The registrars signature must be applied to the deed on making it effective

    When I get the deed from the api
    Then the signature is applied to the deed
    And the date is applied to the deed

Scenario: Deed is Locked from Changes once it is Made Effective

    - Once deed has been made effective, it must locked and no further changes allowed (i.e. any endpoint that updates the deed needs to check whether the deed has been "locked" by the registrar before applying the change to the DB)

    When I try to update the status
    Then I should get a 403 response
