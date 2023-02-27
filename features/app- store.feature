Feature: app store
""" 
Confirm that we can browse the app store related pages on our site
"""

Scenario: success for visiting app store and app store details pages
    Given:I navigate to the app store page
    When:I click on the link to app store details
    Then:I should see the details for that app store

