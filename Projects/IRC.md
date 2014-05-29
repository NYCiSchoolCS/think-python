#iSchool IRC Project
**Due:** Monday, June 2nd

## Hello and Goodbye (10 pts)
  * When the user says "hi", the bot should say "hi!" back.
  * When the user says "bye", the bot should say "bye!" back.
  
**Points Breakdown**
* The bot follows the rules outlined above (10 pts)

##  Guess a Number (50 pts)
When the user says "I want to play a game", the bot should pick a random number between 0 and 100. Then it should prompt the user to guess a number (e.g. "Great! Try to guess a number").

From then on, the computer should respond the following way every time the user enters a number:
 * If the guess is correct, the bot should congratulate you 
 * If the guess is too low, the bot should tell you it's too low
 * If the guess is too high, the bot should tell you it's too high

Once the user starts the game, they should be able to continue to send other messages. For example, the user should be able to say "I want to play a game" and then type "hi" and the bot should respond with "hi!".

**Points Breakdown**

* The bot follows the rules outlined above. **(20 pts)**
* The computer picks a random number between 0 - 100. Once the user starts a game, that number doesn't change. **(10 pts)**
* You successfully check if the current user message is a number **(5 pts)**
* Your code is clear and simple. **(5 pts)**
* **[checkpoint #1]** By the end of class 5/8, you sent us your code, and a short note about how much you have done/things you know are broken. For example, you could say "I have the game working, but my bot crashes if you enter a random string." **(10 pts)**

##  Add Your Own Functionality (40 pts)
   Come up with your own idea for a bot. Please let us know what you want to make before you start writing code. It does not need to be complicated, but it does need to be your own idea.

**Points Breakdown**

* **[checkpoint #2]** You send us an email with a detailed description of your bot idea. You should answer the four questions listed below about how your bot will work. If your idea has changed, we need an email with your final idea so we can check if your code works as intented. **(20 pts)**
* Your bot funtions as you describe in your email. **(10 pts)**
* Your code is clear and simple. You don't have variables or libraries that are never used. If there's anything that is complicated, you add a comment explaining what is going on. **(10 pts)**

=========================
#### Checkpoint #2 Details (Bot Proposal)

You need to send us an email with the answers to the following questions. Copy and paste the questions into the email first.

1. Describe what your bot command will do. 
3. How will your bot know you are using/starting your command? 
2. Does your command happen with one message, or take many messages? What are the messages? 
4. If your command takes many messages, how will your bot know the command is done/over?

Example answers:

1. Describe what your bot command will do.
   
   _My command lets you play a number game. The bot picks a random number and then you try to guess the number. The bot will tell you if your guess is too high or too low to help you guess._

3. How will your bot know you are using/starting your command?
   
   _You will say "I want to play a game" Then the bot will pick a random number, and tell you how to play the game._

2. Does your command happen with one message, or take many messages? What are the messages?
   
   _Many messages, first the "I want to play a game" message, and then all the numbers the user guesses._

4. If your command takes many messages, how will your bot know the command is done/over?
   
   _The game command is over when you guess the correct number._

=========================
#### Testing

You should always thoroughly test your code, here are some things we would like you to test. Please go through these tests and make sure they all work as expected.

1. Start your bot, type in a random string your bot doesn't recognize. _Your bot should not crash._
2. Type "I want to play a game". _Your bot should say the game has started._
3. Type the number 0. _Your bot should say the number is too low._
4. Type the number 101. _Your bot should say the number is too high._
5. Type in a random string again. _Your bot should not crash._
6. Play the rest of the game. _When you guess the right number, your bot should say you won._
8. Type "I want to play a game" again. _Your bot should say the game has started._
9. Play the game. _The correct number should be different than the first game._

Bonus Tests! These are "nice to haves" that make things easier on the person using your code.

1. Type "i want to play a game". _Your bot should say the game has started._
2. Type "I WANT TO PLAY A GAME". _Your bot should say the game has started._
3. Restart your bot, and enter a number. _Your bot should say there's no game running._
4. Play the game and then enter the winning number again. _Your bot should say there's no game running._

=========================
#### Some useful commands:

* The function randrange takes in two parameters and returns a random integer between them. For example, ```randrange(-10, 10)``` will return a random number between -10 and 10.

* You can check if a string could be turned into an integer by using the isdigit function. For example, ```"123".isdigit()``` returns true and ```"hey1".isdigit()``` returns false.

* If you want to change a global variable inside a function, you have to add an extra line in your function to reference that variable. See the example below. If you don't have the line "global my_name", then Python will throw an error.
my_name = "erica"

```python
my_name = ""
def change_name():
    global my_name
    my_name = "erica greene"
```
=========================
#### History of IRC
IRC, short for Internet Relay Chat, is a chat messaging system that allows users to send text messages to each other in discussion forums (called "channels"). IRC was created by Jarkko Oikarinen in August 1988 in Fineland, but it didn't become popular until the early 1990s. The top 100 IRC networks now served more than half a million users at a time.

Here is the information for the IRC server we set up for iSchool:

* **IP Address:** 54.84.9.196
* **Public DNS:** ec2-54-84-9-196.compute-1.amazonaws.com
* **Port:** 6667
* **IRC Client:** [https://kiwiirc.com/client](https://kiwiirc.com)


**Common IRC commands**
* **/me** Type /me 'does anything'. For example, "/me waves hello" and it will look like: "* erica waves hello"
* **/whois** Type /whois nickname to see a bit more information about another user.
* **/join** Type '/join something' to join a channel. For example, /join #CS101 will join the channel #CS101.
