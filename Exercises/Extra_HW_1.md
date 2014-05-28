# Validate a credit card number

Write a function validate_cc() that takes a credit card number as input and prints "Not a valid credit card" or prints "This card is a X" where X is Visa, MasterCard, American Express, or Discover.

You can tell what type of crdit card its from the number. The first digit is different for each type of credit card and they each have rules for the second digit. Here's the rules for Visa, MasterCard, American Express, and Discover:


 Type            | Starts with...  | Second digit | length 
-------------    | ------------- | -------------    | -------------
American Express |               3 |  4 or 7 | 15 digits
Discover | 6 |  0, 5 or 2 | 16 digits
MasterCard | 5 | Between 1 and 5 | 16 digits
Visa | 4 | Anything | 13 or 16 digits
  
  You can use these test numbers for testing your function: http://www.paypalobjects.com/en_US/vhelp/paypalmanager_help/credit_card_numbers.htm

  Hint: use len() to check the length of a string. Use x[0] to get the first character of string x.
  
