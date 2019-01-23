#!/usr/bin/python
# -*- coding: utf-8 -*-

from until.extract_data import ex_data
from until.crypt import crypt
from until.sshclient import ssh_Client

def run_off_line(dict_path, pw_path):
    data_pw_dict = ex_data(dict_path)
    pw_data = ex_data(pw_path)
    data_dict = data_pw_dict.ex_data_dict()
    data_pw = pw_data.ex_data_dict()
    run_decipher(data_pw, data_dict)

def run_on_line(dict_path, ip, port, username, passwd):
    #ip = input('ip=')
    #port = input('port=')
    #username = input('username=')
    #passwd = input('pw=')
    ssh_data = ssh_Client(ip, port, username, passwd)
    pw_data = ssh_data.connet()
    print(pw_data)
    data_pw_dict = ex_data(dict_path)
    data_dict = data_pw_dict.ex_data_dict()
    data_pw = str(pw_data).split('\n')
    run_decipher(data_pw, data_dict)

def run_decipher(data_pw, data_dict):
    for pw_val in data_pw:
        print(pw_val)
        try:
            if pw_val != '':
                pw_value = str(pw_val).split(':')
                username = pw_value[0]
                if pw_value[1] != '*' and pw_value[1] != '!' and pw_value[1] != '!!':
                    salt = str(pw_value[1])[0:12]
                    pw = str(pw_value[1])[12:len(pw_value[1])]
                    for data_dict_vale in data_dict:
                        pw_dict = crypt(data_dict_vale, salt)
                        pw_dict_list = str(pw_dict).split('$')
                        if pw_dict_list[len(pw_dict_list)-1] == pw:
                            print(username, data_dict_vale)
        except:
            print(pw_val)