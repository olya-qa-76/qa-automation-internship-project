Feature: Tests for Off-Plan feature

  Scenario: User can filter by Announced
    Given Open the main page
    When Log in to the page with email: "valid_email" and password: "valid_password"
    Then Click on "Off-plan" at the left side menu
    And Verify the right page opens
    When Filter by sale status of “Announced”
    Then Verify each product contains the Announced