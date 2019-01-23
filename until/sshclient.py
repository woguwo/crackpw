#!/usr/bin/python
# -*- coding: utf-8 -*-

import paramiko
import time

class ssh_Client:
    def __init__(self, ip, port, user, pw):
        self.ip = ip
        self.port = port
        self.user = user
        self.pw = pw

    def connet(self):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, self.port, self.user, self.pw)
        stdin, stdout, stderr = ssh.exec_command('cat /etc/shadow')
        data =stdout.read()
        return str(data)

