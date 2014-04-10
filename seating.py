#! /usr/bin/python

from random import shuffle

students = ["Oris", "Miguel", "Axel", "Masum", "Daniel", "Mariella", "Eric",\
            "Jonathan", "Gabriel", "Wesley", "Sam", "Dena", "Celeste", "Cole"]

desk_layout = """
X  X
X  X
X  X
X  X
X  X
XXXX"""

width = max([ len(s) for s in students ])
desk = "| %s |"
desk_bar = " " + "-"*(width+2) + " "
blank = " "*(width+4)

desks = ""
for row in desk_layout.split('\n'):
    desks += row.replace(" ", blank).replace("X", desk_bar) + '\n'
    desks += row.replace(" ", blank).replace("X", desk) + '\n'
    desks += row.replace(" ", blank).replace("X", desk_bar) + '\n'

shuffle(students)
print desks%tuple([ s.center(width) for s in students ])