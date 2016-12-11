from GUIVOTE import *
from threading import Thread
from proxymanager import ProxyManager
import subprocess
import os
import json
import sys
import time
from vote import *

thrd=None
app=wx.App(False)
frame=MyFrame2(None)
frame2=ProxyManager()
try:
	frame.m_textCtrl6000.SetValue("30")
	config=json.loads(open('voteconfig.json','r').read())
	if 'server' in config:
		frame.m_textCtrl6.SetValue(config['server'])
	if 'resource' in config:
		frame.m_textCtrl8.SetValue(config['resource'])
	if 'votername' in config:
		frame.m_textCtrl7.SetValue(config['votername'])
	if "totalconnections" in config:
		frame.m_textCtrl41.SetValue(str(config['totalconnections']))
	if "maxchecks" in config:
		frame.m_textCtrl600.SetValue(str(config["maxchecks"]))
	if "usebroker" in config:
		frame.m_checkBox1.SetValue(config["usebroker"])
	if "timeout" in config:
		frame.m_textCtrl6000.SetValue(str(config["timeout"]))
	if "maxperproxy" in config:
		frame.m_textCtrl06.SetValue(str(config['maxperproxy']))
except:
	pass
def finishhandler(value):
	global votecount,linecount
	if len(value)>=8:
		if value[:8]=="|FINISH|":
			votecount=votecount+1
			wx.CallAfter(frame.m_staticText9.SetLabel,("Votecount:    "+str(votecount)))
			return
	linecount+=1
	if linecount>=100:
		linecount=0
		wx.CallAfter(frame.m_textCtrl9.SetValue,"")
	wx.CallAfter(frame.m_textCtrl9.AppendText,(value+"\n"))
def showmanager(event):
	frame2.Show()
	frame2.SetFocus()
def checkstop(withval=''):
	if frame2.killsignal:
		wx.CallLater(1000,checkstop,withval)
		return
	if withval!='':
		frame.m_textCtrl9.SetValue(withval)
	frame.m_button2.Enable()
def onstop(withval=''):
	if frame.m_button2.GetLabel()=="Start":
		return
	frame2.stop()
	frame.m_button2.SetLabel("Start")
	frame.m_button2.Disable()
	checkstop(withval)
def showframe(event):
	frame2.Show()
	frame2.SetFocus()
def execvote(event):
	if frame.m_button2.GetLabel()=='Stop':
		onstop()
		return
	global votecount,linecount
	votecount=0
	linecount=0
	frame.m_textCtrl9.SetValue("")
	server=frame.m_textCtrl6.GetValue()
	resource=frame.m_textCtrl8.GetValue()
	votername=frame.m_textCtrl7.GetValue()
	usebroker=frame.m_checkBox1.GetValue()
	try:
		totalconnections=int(frame.m_textCtrl41.GetValue())
		maxchecks=int(frame.m_textCtrl600.GetValue())
		maxperproxy=int(frame.m_textCtrl06.GetValue())
		timeout=int(frame.m_textCtrl6000.GetValue())
		resource=resource.lower()
		if resource not in ['food','wood','stone','iron']:
			raise
	except:
		return
	frame.m_button2.SetLabel("Stop")
	frame2.MAX_CHECKS=maxchecks
	frame2.MAX_PROCESS=totalconnections
	try:
		d={'server':server,'resource':resource,'usebroker':usebroker,'votername':votername,'totalconnections':totalconnections,'maxchecks':maxchecks,'maxperproxy':maxperproxy}
		f=open('voteconfig.json','w')
		json.dump(d,f)
		f.close()
	except:
		pass
	if usebroker:
		t=Thread(target=frame2.startbroker)
		t.daemon=True
		t.start()
	frame2.startchecker()
	frame2.runprocess(startvote,server,resource,votername,timeout=timeout,totalconn=maxperproxy,callback=finishhandler)
def onclose(event):
	onstop()
	sys.exit()
frame.m_button2.Bind(wx.EVT_BUTTON,execvote)
frame.m_button3.Bind(wx.EVT_BUTTON,showframe)
frame.Bind(wx.EVT_CLOSE,onclose)
frame.Show()
app.MainLoop()
