#! /usr/bin/python

import os
import sys
from os.path import abspath

sdtin = os.getcwd()


class Folder:
    def __init__(self, filename):
        self.filename = filename
        # NOTE Keep it as string to conserve any leading 0
        wrong_date = filename[7:15]
        try:
            if int(wrong_date):
                # NOTE the not (!=)
                if wrong_date[:4] != "2017":
                    year = wrong_date[4:]
                    month = wrong_date[2:4]
                    day = wrong_date[:2]
                    self.correct_date = ''.join([year, month, day])
        except ValueError:
                pass

        self.path = abspath(filename)
