Feature: Add item to basket
  Scenario: add item successfull
    Given I clicked "Electronics" button with acc id
    Given I clicked "com.allandroidprojects.getirsample:id/image1" button with id
    Given I clicked "com.allandroidprojects.getirsample:id/text_action_bottom1" button with id
    When I clicked "com.allandroidprojects.getirsample:id/text_action_bottom2"
    Then I should see "com.allandroidprojects.getirsample:id/text_action_bottom1" with this text "$3.96"
    Then I should see "com.allandroidprojects.getirsample:id/text_action_bottom2" with this text "PAYMENT"

