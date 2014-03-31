# Yahtzee Project

## The Rules
The object of the game is to score the most points by rolling five dice to make certain combinations. The dice can be rolled up to three times in a turn to try to make one of the thirteen possible scoring combinations.

The scoring combinations have varying point values, some of which are fixed values and others of which have the cumulative value of the dice. A Yahtzee is five-of-a-kind and holds the game's highest point value of 50. (*taken from Wikipedia*).

For all rules, see the official instructions [here](http://www.hasbro.com/common/instruct/Yahtzee.pdf)

## Instructions
We wrote [some starter code](Yahtzee.py) for implementing scoring in Yahtzee. The roll_dice function simulates one roll and the values of the five dice are stored in the variables d1, d2, d3, d4 and d5.

Your job is the fill in the ten scoring functions. We wrote the definitions and documentation for the functions, but we haven't filled them in yet.

1. **Implement all the scoring functions in Yahtzee.py. (70 pts)**

    You will noticed that the code for ones_score, twos_score etc. is very similar. It is always a bad idea to have duplicate code in a program, so your second task is to find a way to simplify the implementation of those functions.

2. **Write a new function called n_score that combines the functionality of ones_score, twos_score, etc. The n_score function should take d1 through d5 as parameters as well as an integer n. Comment out your old ones_score, twos_score, etc. and rewrite them using n_score. (20 pts)**

     While the code so far implements some of the functionality of Yahtzee, there are still more to do before it feels like the real game. Your final task is to implement one of the following extra features.

3. **Implement at least one extra feature from the following list:**
   - Tell the user what combination would result in the max score. You can use the built in Python function max(x,y,z,..) which takes one of more numbers and returns the number with the greatest value.
   - Extend the game to two players. The program should ask each player for his or her name and then print out the results of score_roll for each player.
   - Add multiple turns for each player. At each round, the program should tell the player what their current score is.
   - Allow players to choose which combination they want to use at each turns.

### Note: A prize will be given out to the person who has the most full-featured Yahtzee program.

## Rubric

- You have clear and accurate implementions of the following functions:

    | function      | points        |
    | ------------- |:-------------:|
    |    ones_score | 5 pts         |
    |    twos_score | 5 pts         |
    | threes_score  | 5 pts         |
    | fours_score   | 5 pts         |
    | fives_score   | 5 pts         |
    | sixes_score   | 5 pts         |
    | four_of_a_kind_score | 10 pts |
    | five_of_a_kind_score | 10 pts |
    | large_straight | 10 pts       |
    | chance_score | 10 pts         |
    | n_score      | 10 pts         |

- You include documentation for the n_score functions. (10 pts)
- You implement one of the extra features in task 3. (10 pts)
