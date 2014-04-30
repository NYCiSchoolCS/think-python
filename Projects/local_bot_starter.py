import random
BOT_NAME = "mr_bot"

def run_IRC():
    print "Welcome to (local) IRC!"
    username = raw_input("What is your username? ")

    while 1:
        message = raw_input(username + ":\t")
        response = parse_message(message)

        print BOT_NAME + ": " + response

def parse_message(message):
    """
    Parses IRC message and returns a response.
    Remember: all multi-word responses need to start with colon (:)
    """
    return ""


############################# Main Progrm #####################################
run_IRC()
