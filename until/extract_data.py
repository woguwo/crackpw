#!/usr/bin/python
# -*- coding: utf-8 -*-

class ex_data:
    def __init__(self, file):
        self.file = file
        self.data_pw = []

    def ex_data_dict(self):
        with open(self.file, 'r') as f:
            for line in f.readlines():
                self.data_pw.append(str(line).replace('\n',''))
        #print(self.data_pw)
        return self.data_pw
