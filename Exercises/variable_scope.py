# 1 ***************************

def print_all():
    print X, Y, Z,

def setup():
    X = 4
    Y = 6
    Z = 5

setup()
print_all()

# 2 ***************************

X = 5
Y = 3

def add(a, b):
    print X + Y

add(2, 4)

# 3 ***************************

def switch_cat(a, b):
    print a, b
    print b, a

print a, b

# 4 ***************************

word = "winning"

def emphasize(string):
    print "*" + string + "*"
    
print emphasize, word
print string

# 5 ***************************

def this():
    X = 4
    print X,  Y

def that(Y):
    print Y

this()