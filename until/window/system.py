#!/usr/bin/python
# -*- coding: utf-8 -*-


import platform
s = platform.system()
del platform

def isLinux():
	return s == 'Linux'

def isDarwin():
	return s == 'Darwin'

def isWindows():
	return s == 'Windows'