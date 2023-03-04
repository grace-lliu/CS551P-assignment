Feature: app store
  """
  Confirm that we can browse the app store related pages on our site
  """
  
  Scenario: success for visiting app store and app store details pages
    Given the app store page is available
    When I navigate to the app details page with id "281656475"
    Then the URL should include the app ID
