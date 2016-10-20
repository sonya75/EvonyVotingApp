from GUIVOTE import *
from threading import Thread
import subprocess
import os
import json
import sys
import time
thrd=None
app=wx.App(False)
frame=MyFrame2(None)
votecount=0
def killvote(pid,triedone=False):
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	subprocess.Popen(["TASKKILL","/F","/T","/pid",str(pid)],startupinfo=startupinfo)
	if not triedonce:
		wx.CallLater(1000,killvote,pid,True)
def onclose(event):
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	subprocess.Popen(["TASKKILL","/F","/im","vote.exe"],startupinfo=startupinfo)
	sys.exit()
def checkprocess():
	global voteprocess,lastupdate
	try:
		if (frame.m_button2.GetLabel())=="Start":
			return
		else:
			if (time.time()-lastupdate)>15:
				try:
					ppid=voteprocess.pid
					killvote(ppid)
				except:
					pass
				lastupdate=time.time()
				frame.m_textCtrl9.SetValue("Error in connection or the price of the resource is above 0.05. Trying again.")
				wx.CallLater(100,execvote,None)
				return
			wx.CallLater(1000,checkprocess)
	except:
		wx.CallLater(1000,checkprocess)
		return
frame.Bind(wx.EVT_CLOSE,onclose)
if os.path.exists('voteconfig.json'):
	try:
		config=json.loads(open('voteconfig.json','r').read())
		if 'server' in config:
			frame.m_textCtrl6.SetValue(config['server'])
		if 'resource' in config:
			frame.m_textCtrl8.SetValue(config['resource'])
		if 'votername' in config:
			frame.m_textCtrl7.SetValue(config['votername'])
	except:
		pass
def handletext(value):
	global lastupdate
	lastupdate=time.time()
	frame.m_textCtrl9.write(value)
def handleerror(value):
	global lastupdate,voteprocess
	try:
		killvote(voteprocess.pid)
	except:
		pass
	lastupdate=time.time()
	if value==1:
		frame.m_textCtrl9.SetValue("Invalid resource. Possible resource types are food or lumber or stone or iron")
		frame.m_button2.SetLabel("Start")
		frame.m_textCtrl6.Enable()
		frame.m_textCtrl7.Enable()
		frame.m_textCtrl8.Enable()
		return
	if value==2:
		frame.m_textCtrl9.SetValue("Invalid Name. Enter again.")
		frame.m_button2.SetLabel("Start")
		frame.m_textCtrl6.Enable()
		frame.m_textCtrl7.Enable()
		frame.m_textCtrl8.Enable()
		return
	if value==0:
		frame.m_textCtrl9.SetValue("Error while building account. Trying again in 1 seconds.")
		wx.CallLater(1000,execvote,None)
def finishhandler():
	global votecount
	votecount=votecount+1
	frame.m_staticText9.SetLabel("Votecount:    "+str(votecount))
def fff(comm):
	global voteprocess
	startupinfo = subprocess.STARTUPINFO()
	startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
	p=subprocess.Popen(comm,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,startupinfo=startupinfo)
	voteprocess=p
	for q in p.stdout:
		if "ERRORINVALIDRES" in q:
			wx.CallAfter(handleerror,1)
			break
		if "ERRORINVALIDNAME" in q:
			wx.CallAfter(handleerror,2)
			break
		if 'ERRORREPORT' in q:
			wx.CallAfter(handleerror,0)
			break
		if 'FINISHREPORT' in q:
			wx.CallAfter(finishhandler)
			continue
		wx.CallAfter(handletext,q)
def execvote(event):
	global thrd,votecount,voteprocess,lastupdate
	if ((frame.m_button2.GetLabel())=="Stop")&(event!=None):
		try:
			killvote(voteprocess.pid)
		except:
			pass
		frame.m_textCtrl6.Enable()
		frame.m_textCtrl7.Enable()
		frame.m_textCtrl8.Enable()
		frame.m_button2.SetLabel("Start")
		return
	if (event==None)&((frame.m_button2.GetLabel())=="Start"):
		return
	if event!=None:
		votecount=0
		frame.m_staticText9.SetLabel("Votecount:    0")
	frame.m_button2.SetLabel("Stop")
	frame.m_textCtrl9.SetValue("Starting to build account for voting....")
	server=frame.m_textCtrl6.GetValue()
	resource=frame.m_textCtrl8.GetValue()
	votername=frame.m_textCtrl7.GetValue()
	frame.m_textCtrl6.Disable()
	frame.m_textCtrl7.Disable()
	frame.m_textCtrl8.Disable()
	try:
		f=open('voteconfig.json','w')
		d={'server':server,'resource':resource,'votername':votername}
		json.dump(d,f)
		f.close()
	except:
		pass
	thrd=Thread(target=fff,args=(["vote.exe",server,resource,votername],))
	thrd.daemon=True
	thrd.start()
	lastupdate=time.time()
	wx.CallLater(1000,checkprocess)
frame.m_button2.Bind(wx.EVT_BUTTON,execvote)
frame.Show()
app.MainLoop()