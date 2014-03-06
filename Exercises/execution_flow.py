def greeting():
    print "Hello!"

def fairwell():
    print "Good bye!"

def apology(how_sorry):
    print "I'm",
    print "very "*how_sorry,
    print "sorry"

def arriving_late():
    greeting()
    apology(3)
    print "I'm late"

def on_time():
    greeting()
    print "Nice to see you"

def leaving():
    fairwell()
    print "See you soon!"
    
# Ex 1
arriving_late()
print "..."
fairwell()

# Ex 2
on_time()
print "..."
fairwell()

# Ex 3 (White rabbit)
greeting()
fairwell()
arriving_late()
fairwell()