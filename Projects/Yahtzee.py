from random import randint

def roll_die():
    """
    This function returns a random integer x such that 1 <= x <= 6.
    """
    return randint(1, 6)

def sort(d1, d2, d3, d4, d5):
    """
    This function takes five numbers and returns the numbers in sorted
    order.
    """
    return sorted([d1, d2, d3, d4, d5])

def roll_dice():
    """
    This function returns one Yahtzee roll. Each roll is five integers
    between 1 and 6, inclusive. We return the numbers from smallest to
    to largest.
    """
    d1 = roll_die()
    d2 = roll_die()
    d3 = roll_die()
    d4 = roll_die()
    d5 = roll_die()

    return sort(d1, d2, d3, d4, d5)

def ones_score(d1, d2, d3, d4, d5):
    """
    Your score is the sum of the dice that are one. For example, if your
    roll is 1,2,5,6,6, your ones_score is 1.
    """
    return 0

def twos_score(d1, d2, d3, d4, d5):
    """
    Your score is the sum of the dice that are two. For example, if your
    roll is 1,2,5,6,6, your twos_score is 2.
    """
    return 0

def threes_score(d1, d2, d3, d4, d5):
    """
    Your score is the sum of the dice that are three. For example, if your
    roll is 1,2,5,6,6, your threes_score is 0.
    """
    return 0

def fours_score(d1, d2, d3, d4, d5):
    """
    Your score is the sum of the dice that are four. For example, if your
    roll is 1,2,5,6,6, your fours_score is 0.
    """
    return 0

def fives_score(d1, d2, d3, d4, d5):
    """
    Your score is the sum of the dice that are five. For example, if your
    roll is 1,2,5,6,6, your fives_score is 5.
    """
    return 0

def sixes_score(d1, d2, d3, d4, d5):
    """
    Your score is the sum of the dice that are six. For example, if your
    roll is 1,2,5,6,6, your sixes_score is 12.
    """
    return 0

def four_of_a_kind_score(d1, d2, d3, d4, d5):
    """
    If four out of the five die are the same number, your score is the sum
    of all five of the die. Otherwise, your score is 0.
    """
    return 0

def five_of_a_kind_score(d1, d2, d3, d4, d5):
    """
    If all five die are the same number, your score is 50.
    Otherwise, your score is 0
    """
    return 0

def chance_score(d1, d2, d3, d4, d5):
    """
    Your score is the sum of all of the die.
    """
    return 0

def score_roll(d1, d2, d3, d4, d5):
    print "Your roll: ", d1, d2, d3, d4, d5
    print ""
    print "\t ones score:   ", ones_score(d1, d2, d3, d4, d5)
    print "\t twos score:   ", twos_score(d1, d2, d3, d4, d5)
    print "\t threes score: ", threes_score(d1, d2, d3, d4, d5)
    print "\t fours score:  ", fours_score(d1, d2, d3, d4, d5)
    print "\t fives score:  ", fives_score(d1, d2, d3, d4, d5)
    print "\t sixes score:  ", sixes_score(d1, d2, d3, d4, d5)
    print ""
    print "\t four of a kind: ", four_of_a_kind_score(d1, d2, d3, d4, d5)
    print "\t five of a kind: ", five_of_a_kind_score(d1, d2, d3, d4, d5)
    print ""
    print "\t chance: ", chance_score(d1, d2, d3, d4, d5)

############################# Main Program ###############################
print "Thanks for playing Yahtzee!\n"

d1, d2, d3, d4, d5 = roll_dice()
score_roll(d1, d2, d3, d4, d5)
