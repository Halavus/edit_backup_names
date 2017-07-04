#! /usr/bin/python

import os
import sys
from os.path import abspath

# sdtin = os.getcwd()


class Folder:
    def __init__(self, filename):
        self.filename = filename
        wrong_date = filename[7:15]
        try:
            if int(wrong_date) and wrong_date[:4] != "2017":
                year = wrong_date[4:]
                month = wrong_date[2:4]
                day = wrong_date[:2]
                self.correct_date = ''.join([year, month, day])
                self.new_path = ''.join([os.getcwd(), "/", filename[:7], 
                    self.correct_date, filename[15:]])
            else:
                self.correct_date = None
                self.new_path = None
        except ValueError:
                self.correct_date = None
                self.new_path = None

        self.path = abspath(filename)
