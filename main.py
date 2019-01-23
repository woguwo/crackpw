#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from until.window.splash import SplashScreen
from until.window.window_main import MainFrame
from until.window import resources
import os


class ShellApp(wx.App):

    def __init__(self):
        resources.setBasePath(os.path.join(os.path.dirname(__file__), "./"))
        super(ShellApp, self).__init__(redirect=False)

        SplashScreen(self.start)
    def start(self):
        mainFrame = MainFrame()
        mainFrame.Show(True)
        icon = wx.Icon()
        icon.LoadFile(".\\until\window\image\main1.ico", wx.BITMAP_TYPE_ICO)
        mainFrame.SetIcon(icon)
        return True


if __name__ == '__main__':
    app = ShellApp()

    app.MainLoop()