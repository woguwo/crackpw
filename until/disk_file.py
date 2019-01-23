#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
class diskwalk(object):
        def __init__(self,path):
                self.path = path
        def paths(self):
                path=self.path
                path_collection=[]
                for dirpath,dirnames,filenames in os.walk(path):
                        for file in filenames:
                                fullpath=os.path.join(dirpath,file)
                                path_collection.append(fullpath)
                return path_collection

if __name__ == '__main__':
        for file in diskwalk('../data/').paths():
                print(file)