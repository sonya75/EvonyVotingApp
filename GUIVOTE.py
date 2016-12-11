# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 579,563 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Server", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		bSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_textCtrl6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl6, 0, wx.ALL, 5 )
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Name of the player you want to vote", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		bSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.m_textCtrl7 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl7, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Resource (example: stone)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		bSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.m_textCtrl8 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_textCtrl8, 0, wx.ALL, 5 )

		self.m_checkBox1 = wx.CheckBox( self, wx.ID_ANY, u"Use Proxybroker", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_checkBox1, 0, wx.ALL, 5 )
		
		bSizer51 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Maximum number of proxies to be used", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer51.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl41 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer51.Add( self.m_textCtrl41, 0, wx.ALL, 0 )
		
		
		bSizer2.Add( bSizer51, 0, wx.EXPAND, 5 )
		
		bSizer7 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText600 = wx.StaticText( self, wx.ID_ANY, u"Maximum number of proxies to be checked simultaneously", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText600.Wrap( -1 )
		bSizer7.Add( self.m_staticText600, 0, wx.ALL, 5 )
		
		self.m_textCtrl600 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_textCtrl600, 0, wx.ALL, 0 )
		
		
		bSizer2.Add( bSizer7, 0, wx.EXPAND, 5 )
		
		bSizer07 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText06 = wx.StaticText( self, wx.ID_ANY, u"Maximum number of connections per proxy", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText06.Wrap( -1 )
		bSizer07.Add( self.m_staticText06, 0, wx.ALL, 5 )
		
		self.m_textCtrl06 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer07.Add( self.m_textCtrl06, 0, wx.ALL, 0 )
		
		
		bSizer2.Add( bSizer07, 0, wx.EXPAND, 5 )

		bSizer900 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText6000 = wx.StaticText( self, wx.ID_ANY, u"Timeout(in seconds)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6000.Wrap( -1 )
		bSizer900.Add( self.m_staticText6000, 0, wx.ALL, 5 )
		
		self.m_textCtrl6000 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer900.Add( self.m_textCtrl6000, 0, wx.ALL, 0 )
		
		
		bSizer2.Add( bSizer900, 0, wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Votecount:    0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		bSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_button2 = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button2, 0, wx.ALL, 5 )
		
		self.m_button3 = wx.Button( self, wx.ID_ANY, u"Proxy-Manager", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.m_button3, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer8, 0, wx.EXPAND, 5 )

		
		self.m_textCtrl9 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_READONLY|wx.TE_WORDWRAP )
		bSizer2.Add( self.m_textCtrl9, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

