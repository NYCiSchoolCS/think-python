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

## Your Bot Assignments (15 pts)
#### Hello and Goodbye
  When you say "hi", the bot should say "hi!" back and when you say "bye", the bot should say back "bye!".


### Guess a Number (70 pts)
  When you say "I want to play a game", the bot should pick a random number between
0 and 100. Then it should prompt you to guess a number.

* If you guess the number, the bot should congratulate you

* If you guess a number that is too low, the bot should tell you it's too low

* If you guess a number that is too high, the bot should tell you it's too high

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

## Make Your Own (15 pts)
   Come up with your own idea for a bot. Please let us know what you want to make before you start writing code. It does not need to be complicated, but it does need to be your own idea.
