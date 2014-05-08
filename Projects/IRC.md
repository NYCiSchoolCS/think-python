#iSchool IRC

IRC, short for Internet Relay Chat, is a chat messaging system that allows users to send text messages to each other in discussion forums (called "channels"). IRC was created by Jarkko Oikarinen in August 1988 in Fineland, but it didn't become popular until the early 1990s. The top 100 IRC networks now served more than half a million users at a time.

Here is the information for the IRC server we set up for iSchool:

* **IP Address:** 54.84.9.196
* **Public DNS:** ec2-54-84-9-196.compute-1.amazonaws.com
* **Port:** 6667
* **IRC Client:** [https://kiwiirc.com/client](https://kiwiirc.com)


## Common IRC commands
* **/me** Type /me 'does anything'. For example, "/me waves hello" and it will look like: "* erica waves hello"
* **/whois** Type /whois nickname to see a bit more information about another user.
* **/join** Type '/join something' to join a channel. For example, /join #CS101 will join the channel #CS101.

## Your Bot Assignments 
#### Hello and Goodbye (15 pts)
  When you say "hi", the bot should say "hi!" back and when you say "bye", the bot should say back "bye!".


####  Guess a Number (70 pts)
  When you say "I want to play a game", the bot should pick a random number between
0 and 100. Then it should prompt you to guess a number (e.g. "Great! Try to guess a number"). From now on, if the user guesses a number, the computer should respond the following way:

* If the guess is correct, the bot should congratulate you

* If the guess is too low, the bot should tell you it's too low

* If the guess is too high, the bot should tell you it's too high

Some useful commands:

* The function randrange takes in two parameters and returns a random integer between them. For example, ```randrange(-10, 10)``` will return a random number between -10 and 10.

* You can check if a string could be turned into an integer by using the isdigit function. For example, ```"123".isdigit()``` returns true and ```"hey1".isdigit()``` returns false.

* If you want to change a global variable inside a function, you have to add an extra line in your function to reference that variable. See the example below. If you don't have the line "global my_name", then Python will throw an error.
my_name = "erica"

```python
def change_name():
    global my_name
    my_name = "erica greene"
```

####  Make Your Own (15 pts)
   Come up with your own idea for a bot. Please let us know what you want to make before you start writing code. It does not need to be complicated, but it does need to be your own idea.



## Check point 5/8 (30 points total)

#### (10 pts) By the end of class

Send us your code, and a short note about how much you have done/things you know are broken. For example, you could say "I have the game working, but my bot crashes if you enter a random string."

#### (20 pts) By the end of the week 

Send us an email with the answers to the following questions. Copy and paste the questions into the email first.

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
