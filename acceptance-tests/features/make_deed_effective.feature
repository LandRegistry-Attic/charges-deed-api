@make_deed_effective

Feature: Make Deed Effective
  As a Conveyancer I want to be able to make a deed effective
  So that it is ready for submission to Land Registry

  Background:
    Given I have created a case
    And I have created the following deed:
    """
    {
     "id":"1",
     "mdref": "MD0149A",
     "title": {
       "title-number": "GHR67832",
       "address": {
         "street-address": "18 Lordly Place",
         "extended-address": "",
         "locality": "London",
         "postal-code": "N12 5TN"
       }
     },
     "lender": {
       "name": "Bank of England PLC",
       "company-number": "2347672",
       "address": {
         "street-address": "12 Trinity Place",
         "extended-address": "Regents Street",
         "locality": "London",
         "postal-code": "NW10 6TQ"
       }
     },
     "borrowers":[{
       "id": "1",
       "name": "Peter Smith",
       "address": {
         "street-address": "83 Lordship Park",
         "extended-address": "",
         "locality": "London",
         "postal-code": "N16 5UP"
       }
     }],
     "restrictions": ["This is my restriction"],
     "provisions": ["This Mortgage Deed incorporates the Lenders Mortgage Conditions and Explanation 2006, a copy of which has been received by the Borrower.",
       "The lender is under an obligation to make further advances and applies for the obligation to be entered in the register.",
       "No disposition of the registered estate by the proprietor of the registered estate is to be registered without a written consent signed by Bank of England Plc."]
    }
    """
    And I have linked the created deed and case
    And I have made the created deed effective

  Scenario: Date and Signature Applied when Deed is Made Effective

  - Date must be added to the deed which consists of time stamp (current datetime)
  - The registrars signature must be applied to the deed on making it effective

    When I get the deed from the api
    Then the signature is applied to the deed
    And the date is applied to the deed

  Scenario: Deed is Locked from Changes once it is Made Effective

  - Once deed has been made effective, it must be locked and no further changes allowed (i.e. any endpoint that updates the deed needs to check whether the deed has been "locked" by the registrar before applying the change to the DB)

    When I try to sign the deed again
    Then I should get a 403 response
