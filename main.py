#! /usr/bin/python

import os
from module import Folder as Folder

ls=os.listdir('.')

lsin=[Folder(i) for i in ls]

for i in lsin:
    if i.correct_date:
        os.rename(i.path, i.new_path)
        print i.filename, "-> renamed with", i.correct_date, "successfully"
    else:
        print i.filename, "-> has not been renamed"
