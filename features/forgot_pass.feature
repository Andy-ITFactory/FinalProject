Feature: Jules login test

    Background:
      Given login: user is on the login page

    @tema
    Scenario Outline: Forgot pass cu tabel de valori
      When login: user clicks on forgot pass button
      When forgot_pass: user enters email address in email input "<valid_email>"
      Then forgot_pass: verify that send email button is enabled

    Examples:
      | valid_email             |
      | itfactory1.ro@gmail.com |
      | itfactory2.ro@gmail.com |
      | itfactory3.ro@gmail.com |
