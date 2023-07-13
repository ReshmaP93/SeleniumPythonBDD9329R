Feature: OrangeHRM Logo
  Scenario:Login to orangehrm with valid parameters
    Given I launch chrome browser
    When I open orangehrm homepage
    And Enter username"admin" and password "admin123"
    And click on login button
    Then user must successfully login to the orangehrm application
  Scenario Outline:Login to orangehrm with multiple parameters
    Given I launch chrome browser
    When I open orangehrm homepage
    And Enter username"<username>" and password "<password>"
    And click on login button
    Then user must successfully login to the orangehrm application
    Examples:
      | username  | password |
      | Admin     | admin123 |
      | admin12   | admin1   |





