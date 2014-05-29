# Validate a credit card number

Write a function validate_cc() that takes a credit card number as input and returns "Not a valid credit card" or "This card is a X" where X is Visa, MasterCard, American Express, or Discover.

You can tell what type of crdit card its from the number. The first digit is different for each type of credit card and they each have rules for the second digit. Here's the rules for Visa, MasterCard, American Express, and Discover:


 Type  | Starts with...  | Second digit | length 
------ | --------------- | ------------ | -------
American Express | 3 | 4 or 7 | 15 digits
Discover | 6 |  0, 5 or 2 | 16 digits
MasterCard | 5 | Between 1 and 5 | 16 digits
Visa | 4 | Anything | 13 or 16 digits
  

You can use these numbers to test your function: 

Type  | Test Number 
----- | -----------
American Express | 378282246310005
American Express | 341449635398431
Discover | 6011111111111117
Discover | 6511000990139424
MasterCard | 5555555555554444
MasterCard | 5105105105105100
Visa | 4012888888881881
Visa | 4222222222222

([source](http://www.paypalobjects.com/en_US/vhelp/paypalmanager_help/credit_card_numbers.htm))

Hint: You can use `len()` to check the length of a string and `string[0]` to get the first character of string x.
  
