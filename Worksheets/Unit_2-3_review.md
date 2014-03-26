#Unit 2/3 – Review

1. Write a function that takes a height and a radius of a cylinder and calculates the volume. Recall that the formula for the volume of a cylinder is (2\*pi\*radius^2)*height

1. What is printed when the following code is run?
  ```python
  def function_a():
    print "Hello from A"
    function_c(5)
  
  def function_b():
    print "Hello from B"
    function_a()
  
  def function_c(m):
    if m < 2:
      print "We're at C now"
    else:
      print "C is " + str(m) + " times cooler than B"
  
  def abc():
    function_b()
    print "Hello from xyz"
    function_c(1)
  
  abc()
  ```

1. Does the variable `word` have local or global scope? What about `string`?
  ```python
  word = "winning"
  
  def emphasize(string):
      print "*" + string + "*"
      
  emphasize()
  ```

1. Name one reason to use a function in programming.

1. Describe the difference between a local and a global variable.

1. How many different kinds of boolean values are there? What are they called?

1. Convert the following numbers to binary
  * 8
  * 64
  * 20
  * 79
  * 128

1. Convert the following numbers to decimal
  * 10
  * 110101
  * 10101
  * 1110000101
  
1. Evaluate the following satments as true or false based on this image:  
  * NOT (SpongeBob is in a bubble)
  * Number of animals in bubbles > 3
  * (Snail is blowing a bubble) OR (Snail is inside a bubble)
  * (NOT (Starfish has shoes)) AND (SpongeBob has shoes)
  * All animals are wearing a shirt
  * (NOT (Octopus has eyebrows) AND (Octopus has eyelashes)) OR (NOT (Snail has eyebrows) OR (Snail has eyelashes))
  
  ![spongebob](/images/spongebob-bubbles.jpg)
