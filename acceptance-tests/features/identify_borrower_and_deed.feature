@identify_borrower_and_deed

Feature: Identify Borrowers and Their Deed
  As a borrower
  I want to view my deed
  so that I can sign it

@delete_test_data
Scenario: Tokens Generated on Deed Creation

  - deed api should create tokens when deed is created

  Given I have created a case and deed with two borrowers
  Then the api response contains a token for each borrower
