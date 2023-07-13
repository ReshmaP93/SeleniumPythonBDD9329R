Feature: OrangeHRM Login

  Background: common steps
    Given I launch browser
    When I open orangehrm application
    And Enter valid username and password
    And click on login

  Scenario:Login to orangehrm
    Then user must login to dashboard page

  Scenario:Search User
    When Navigate to search page
    Then Search page should display

  Scenario:Advanced Search User
    When Navigate to advanced search page
    Then Advance Search page should display