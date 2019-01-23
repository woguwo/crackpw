#!/usr/bin/python
# -*- coding: utf-8 -*-


import time
import wx._core
from wx import adv
from until.window.resources import getPathForImage

class SplashScreen(adv.SplashScreen):

	def __init__(self, callback):
		self.callback = callback

		bitmap = wx.Image(getPathForImage("splash.png"), wx.BITMAP_TYPE_PNG).ConvertToBitmap()
		super(SplashScreen, self).__init__(bitmap, adv.SPLASH_CENTRE_ON_SCREEN, 0, None)
		#-- TODO: fix in wx.SplashScreen class
		time.sleep(1)
		#--
		wx.CallAfter(self.DoCallback)

	def DoCallback(self):
		self.Destroy()
		self.callback()