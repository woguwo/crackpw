# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
from deciphering import linux_un

###########################################################################
## Class MyFrame1
###########################################################################

class MainFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title=u"口令破解小工具", pos=wx.DefaultPosition,
                          size=wx.Size(631, 350), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.online_notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_panel8 = wx.Panel(self.online_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        main_Sizer = wx.FlexGridSizer(7, 2, 0, 0)
        main_Sizer.SetFlexibleDirection(wx.BOTH)
        main_Sizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.onliine_staticText = wx.StaticText(self.m_panel8, wx.ID_ANY, u"请输入以下信息", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.onliine_staticText.Wrap(-1)
        main_Sizer.Add(self.onliine_staticText, 0, wx.ALL, 5)

        self.sign_staticText = wx.StaticText(self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.sign_staticText.Wrap(-1)
        main_Sizer.Add(self.sign_staticText, 0, wx.ALL, 5)

        self.ip_Text = wx.StaticText(self.m_panel8, wx.ID_ANY, u"IP地址：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.ip_Text.Wrap(-1)
        main_Sizer.Add(self.ip_Text, 0, wx.ALL, 5)

        self.ip_textCtrl = wx.TextCtrl(self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        main_Sizer.Add(self.ip_textCtrl, 0, wx.ALL, 5)

        self.port_Text = wx.StaticText(self.m_panel8, wx.ID_ANY, u"端口号：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.port_Text.Wrap(-1)
        main_Sizer.Add(self.port_Text, 0, wx.ALL, 5)

        self.port_textCtrl = wx.TextCtrl(self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         0)
        main_Sizer.Add(self.port_textCtrl, 0, wx.ALL, 5)

        self.usernaem_Text = wx.StaticText(self.m_panel8, wx.ID_ANY, u"用户名：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.usernaem_Text.Wrap(-1)
        main_Sizer.Add(self.usernaem_Text, 0, wx.ALL, 5)

        self.username_textCtrl = wx.TextCtrl(self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        main_Sizer.Add(self.username_textCtrl, 0, wx.ALL, 5)

        self.passwd_Text = wx.StaticText(self.m_panel8, wx.ID_ANY, u"密码：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.passwd_Text.Wrap(-1)
        main_Sizer.Add(self.passwd_Text, 0, wx.ALL, 5)

        self.passwd_textCtrl = wx.TextCtrl(self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                           0)
        main_Sizer.Add(self.passwd_textCtrl, 0, wx.ALL, 5)

        self.m_staticText16 = wx.StaticText(self.m_panel8, wx.ID_ANY, u"字典文件", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText16.Wrap(-1)
        main_Sizer.Add(self.m_staticText16, 0, wx.ALL, 5)

        self.dict_dirPicker = wx.DirPickerCtrl(self.m_panel8, wx.ID_ANY, wx.EmptyString, u"Select a folder",
                                               wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        main_Sizer.Add(self.dict_dirPicker, 0, wx.ALL, 5)

        self.sign_staticText12 = wx.StaticText(self.m_panel8, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.sign_staticText12.Wrap(-1)
        main_Sizer.Add(self.sign_staticText12, 0, wx.ALL, 5)

        self.online_start_button = wx.Button(self.m_panel8, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0)
        main_Sizer.Add(self.online_start_button, 0, wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.online_check_linux, self.online_start_button)

        self.m_panel8.SetSizer(main_Sizer)
        self.m_panel8.Layout()
        main_Sizer.Fit(self.m_panel8)
        self.online_notebook.AddPage(self.m_panel8, u"在线检测", True)
        self.m_panel9 = wx.Panel(self.online_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer2 = wx.FlexGridSizer(4, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.sign_staticText = wx.StaticText(self.m_panel9, wx.ID_ANY, u"请输入以下信息", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.sign_staticText.Wrap(-1)
        fgSizer2.Add(self.sign_staticText, 0, wx.ALL, 5)

        self.sign_staticText9 = wx.StaticText(self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.sign_staticText9.Wrap(-1)
        fgSizer2.Add(self.sign_staticText9, 0, wx.ALL, 5)

        self.passwd_path_Text = wx.StaticText(self.m_panel9, wx.ID_ANY, u"密码文件", wx.DefaultPosition, wx.DefaultSize, 0)
        self.passwd_path_Text.Wrap(-1)
        fgSizer2.Add(self.passwd_path_Text, 0, wx.ALL, 5)

        self.passwd_dirPicker = wx.DirPickerCtrl(self.m_panel9, wx.ID_ANY, wx.EmptyString, u"Select a folder",
                                             wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        fgSizer2.Add(self.passwd_dirPicker, 0, wx.ALL, 5)

        self.dict_path_Text = wx.StaticText(self.m_panel9, wx.ID_ANY, u"字典文件", wx.DefaultPosition, wx.DefaultSize, 0)
        self.dict_path_Text.Wrap(-1)
        fgSizer2.Add(self.dict_path_Text, 0, wx.ALL, 5)

        self.dict_path_dirPicker = wx.DirPickerCtrl(self.m_panel9, wx.ID_ANY, wx.EmptyString, u"Select a folder",
                                             wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        fgSizer2.Add(self.dict_path_dirPicker, 0, wx.ALL, 5)

        self.sign_staticText13 = wx.StaticText(self.m_panel9, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.sign_staticText13.Wrap(-1)
        fgSizer2.Add(self.sign_staticText13, 0, wx.ALL, 5)

        self.offline_start_button = wx.Button(self.m_panel9, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.offline_start_button, 0, wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, self.offline_check_linux, self.offline_start_button)

        self.m_panel9.SetSizer(fgSizer2)
        self.m_panel9.Layout()
        fgSizer2.Fit(self.m_panel9)
        self.online_notebook.AddPage(self.m_panel9, u"离线检测", False)
        self.m_panel10 = wx.Panel(self.online_notebook, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gSizer7 = wx.GridSizer(2, 2, 0, 0)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel10, wx.ID_ANY, u"在线批量"), wx.VERTICAL)

        fgSizer10 = wx.FlexGridSizer(2, 2, 0, 0)
        fgSizer10.SetFlexibleDirection(wx.BOTH)
        fgSizer10.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.policy_staticText17 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"配置文件", wx.DefaultPosition, wx.DefaultSize,
                                                 0)
        self.policy_staticText17.Wrap(-1)
        fgSizer10.Add(self.policy_staticText17, 0, wx.ALL, 5)

        self.policy_online_dirPicker = wx.DirPickerCtrl(self.m_panel10, wx.ID_ANY, wx.EmptyString, u"Select a folder",
                                                        wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        fgSizer10.Add(self.policy_online_dirPicker, 0, wx.ALL, 5)

        self.m_staticText17 = wx.StaticText(self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText17.Wrap(-1)
        fgSizer10.Add(self.m_staticText17, 0, wx.ALL, 5)

        self.online_batch_button = wx.Button(self.m_panel10, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer10.Add(self.online_batch_button, 0, wx.ALL, 5)

        sbSizer1.Add(fgSizer10, 1, wx.EXPAND, 5)

        gSizer7.Add(sbSizer1, 1, wx.EXPAND, 5)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel10, wx.ID_ANY, u"离线批量"), wx.VERTICAL)

        fgSizer11 = wx.FlexGridSizer(2, 2, 0, 0)
        fgSizer11.SetFlexibleDirection(wx.BOTH)
        fgSizer11.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText18 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"文件路径", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText18.Wrap(-1)
        fgSizer11.Add(self.m_staticText18, 0, wx.ALL, 5)

        self.policy_offline_dirPicker = wx.DirPickerCtrl(self.m_panel10, wx.ID_ANY, wx.EmptyString, u"Select a folder",
                                                         wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        fgSizer11.Add(self.policy_offline_dirPicker, 0, wx.ALL, 5)

        self.m_staticText181 = wx.StaticText(self.m_panel10, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.m_staticText181.Wrap(-1)
        fgSizer11.Add(self.m_staticText181, 0, wx.ALL, 5)

        self.offline_batch_button = wx.Button(self.m_panel10, wx.ID_ANY, u"开始", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer11.Add(self.offline_batch_button, 0, wx.ALL, 5)

        sbSizer3.Add(fgSizer11, 1, wx.EXPAND, 5)

        gSizer10 = wx.GridSizer(1, 1, 0, 0)

        self.m_staticText20 = wx.StaticText(self.m_panel10, wx.ID_ANY, u"离线批量检测：检测文件格式为父目录。", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText20.Wrap(-1)
        gSizer10.Add(self.m_staticText20, 0, wx.ALL | wx.EXPAND, 5)

        sbSizer3.Add(gSizer10, 1, wx.EXPAND, 5)

        gSizer7.Add(sbSizer3, 1, wx.EXPAND, 5)

        self.m_panel10.SetSizer(gSizer7)
        self.m_panel10.Layout()
        gSizer7.Fit(self.m_panel10)
        self.online_notebook.AddPage(self.m_panel10, u"批量检测", True)

        bSizer1.Add(self.online_notebook, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(bSizer1)
        self.Layout()

    def online_check_linux(self, event):
        ip = self.ip_textCtrl.GetValue()
        port = self.port_textCtrl.GetValue()
        username = self.username_textCtrl.GetValue()
        passwd = self.passwd_textCtrl.GetValue()
        policy = str(self.dict_dirPicker.GetPath())
        linux_un.run_on_line(policy, ip, port, username, passwd)

    def offline_check_linux(self, event):
        passwd_path = self.passwd_dirPicker.GetPath()
        dict_path = self.dict_path_dirPicker.GetPath()
        linux_un.run_off_line(dict_path, passwd_path)
