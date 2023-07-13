Feature: OrangeHRM Logo
  Scenario:Logo presence on orangehrm homepage
    Given launch chrome browser
    When open orangehrm homepage
    Then verify that logo present on homepage
    And closebrowser

