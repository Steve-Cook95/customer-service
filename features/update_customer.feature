Feature: updating customer information on request
  
    Scenario: Successful customer name change
        Given customer "Mary Jane" with ID "23456" exists
        When I change customer with ID "23456" name to "Mary Pot"
        Then I should see customer "Mary Pot"