# Something's not quite right in all these code
# examples. Try to spot the mistake!
#
# Assume that all the variables are defined.

# 1 ***************************

if operation = "add":
    print x + y

if operation = "subtract":
    print x - y

# 2 ***************************

if name == "amy" or "erica":
    print "You're a teacher"
elif name == "brian" or "mike":
    print "You're a TA"
else:
    print "You're a student"
    
# 3 ***************************

if weight < 10:
    print "This is light as a feather"
if weight > 1000:
    print "This item weighs a TON!"
else:
    print "This item is a very normal weight"

# 4 ***************************

if cost < account_balance:
    print "You can buy this, but you shouldn't"
elif cost < account_balance/2:
    print "You can buy this, and have money left over!"

# 5 ***************************

if temperature > 70:
    print 'Wear shorts.'
elif:
    print 'Wear long pants.'
    
# 6 ***************************

if score < 50:
    print 'F'
elif score >= 60:
    print 'D'
elif score >= 70:
    print 'C'
elif score >= 80:
    print 'B'
elif score >= 90:
    print 'A'
