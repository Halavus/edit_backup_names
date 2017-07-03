#! /usr/bin/python

import os
from main import Folder as Folder

ls=os.listdir('.')

lsin=[Folder(i) for i in ls]

counter = 0
for i in lsin:
    try:
        print "lsin: ", counter, i.path, i.correct_date 
    except AttributeError:
        print ""
    counter += 1
