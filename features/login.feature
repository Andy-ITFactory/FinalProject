Feature: Jules login test

    # BDD - behavior driven development
    # are rolul de a facilita/usura comunicarea in echipa

    # se ruleaza inainte de fiecare test
    Background:
      Given login: user is on the login page

    @smoke
    Scenario: Login fara tabel de valori
      When login: user enters valid username "itfactory.ro@gmail.com" and valid password "pass123"
      Then login: verify that invalid credentials error is displayed


    @smoke
    Scenario Outline: Login cu tabel de valori
      When login: user enters valid username "<email>" and valid password "<pass>"
      Then login: verify that invalid credentials error is displayed

    Examples:
      | email                   | pass      |
      | itfactory1.ro@gmail.com | password1 |
      | itfactory2.ro@gmail.com | password2 |
      | itfactory3.ro@gmail.com | password3 |
