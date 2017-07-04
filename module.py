#! /usr/bin/python

import os
import sys
from os.path import abspath

# sdtin = os.getcwd()


class Folder:
    def __init__(self, filename):
        self.filename = filename
        # indices == indice of each occurence of "-"
        indices = [i for i, x in enumerate(filename) if x == "-"]
        try:
            wrong_date = filename[indices[0]+1:indices[1]]
        except IndexError:
            wrong_date = None
        try:
            if int(wrong_date) and wrong_date[:4] != "2017":
                year = wrong_date[4:]
                month = wrong_date[2:4]
                day = wrong_date[:2]
                self.correct_date = ''.join([year, month, day])
                self.new_path = ''.join([
                    os.getcwd(), "/",
                    filename[:indices[0]+1],
                    self.correct_date, filename[indices[1]:]
                    ])
            else:
                self.correct_date = None
                self.new_path = None
        # TypeError would be if int(None) "NoneType"
        except (ValueError, TypeError) as e:
                self.correct_date = None
                self.new_path = None

        self.path = abspath(filename)
