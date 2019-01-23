#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from until.disk_file import diskwalk


class SwitchBoard:
    def __init__(self):
        pass
    def data_trans(self, path_sw):
        self.open_data(path_sw)
    def open_data(self, path_sw):
        data = []
        re_express_cipher = r'cipher.*\n'
        re_express_cisco = r'secret.*\n|md5.*\n'
        re_express_pw = r'password 7.*\n'
        re_express_clearText = r'snmp-server community.*\n'
        with open(path_sw, 'r') as f:
            data.append(['\n\n' + path_sw + '\n'])
            for line in f.readlines():
                data_find_cisco = re.findall(re_express_cisco, str(line))
                data_find_cipher = re.findall(re_express_cipher, str(line))
                data_find_pw = re.findall(re_express_pw, line)
                data_find_clearText = re.findall(re_express_clearText,line)
                #print(len(data_find_cisco))
                if len(data_find_cipher) != 0:
                    data.append(data_find_cipher)
                    #print(data_find_cipher)
                elif len(data_find_cisco) != 0:
                    data.append(data_find_cisco)
                    #print(data_find_cisco)
                elif len(data_find_pw) != 0:
                    data.append(data_find_pw)
                    #print(data_find_pw)
                elif len(data_find_clearText) != 0:
                    data.append(data_find_clearText)
        path_write_pw_l = str(path_sw).split('\\')
        path_write_pw = '\\'.join(str(i) for i in
                                  path_write_pw_l[0:len(path_write_pw_l) - 2]) + '\\data_pw.txt'
        with open(path_write_pw, 'a+') as f:
            f.write(''.join(str(i[0]) for i in data))


if __name__ == '__main__':
    sw = SwitchBoard()
    files = diskwalk('../data/')
    for file in files.paths():
        sw.data_trans(file)