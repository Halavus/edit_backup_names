#! /usr/bin/python

import os
from module import Folder as Folder

ls=os.listdir('.')

lsin=[Folder(i) for i in ls]

counter = 0
for i in lsin:
    print "lsin: ", counter, i.path, i.new_path
    counter += 1

for i in lsin:
    if i.correct_date:
        os.rename(i.path, i.new_path) 
