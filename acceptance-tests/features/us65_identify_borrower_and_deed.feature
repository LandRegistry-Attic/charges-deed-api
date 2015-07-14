@US65

Feature: Identify Borrowers and Their Deed
    As a borrower
    I want to view my deed
    so that I can sign it

Scenario: Tokens Generated on Deed Creation

    - deed api should create tokens when deed is created
    - each borrower has a unique id

    Given I have created the following deed:
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
     },{
       "id": "2",
       "name": "Sarah Jane Smith",
       "address": {
         "street-address": "25 Hanger Lane",
         "extended-address": "Harrow",
         "locality": "London",
         "postal-code": "N11 8RD"
       }
     }],
     "restrictions": ["This is my restriction"],
     "provisions": ["This Mortgage Deed incorporates the Lenders Mortgage Conditions and Explanation 2006, a copy of which has been received by the Borrower.",
       "The lender is under an obligation to make further advances and applies for the obligation to be entered in the register.",
       "No disposition of the registered estate by the proprietor of the registered estate is to be registered without a written consent signed by Bank of England Plc."]
    }
    """
    When I get the created deed from the api
    Then the api response contains a token for each borrower
    And each borrower token should be unique
