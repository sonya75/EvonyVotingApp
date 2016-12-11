from evony import *
import time
import os
import sys
from actionfactory.builder import *
from actionfactory.quest import *
from actionfactory.items import *
from threading import Thread
restypes={'food':0,'lumber':1,'stone':2,'iron':3}
quests={'food':499,'lumber':500,'stone':501,'iron':502}
def createacc(server,resource,votername,proxy=None,proxytype='HTTP',useclient=None,callback=None,timeout=30):
	global restypes,quests
	invalidname=False
	tradeproblem=False
	def th(youa):
		return
	try:
		restype=restypes[resource]
		questtype=quests[resource]
		if proxy.count(':')!=1:
			proxyhost=''
			proxyport=0
			useproxy=False
		else:
			useproxy=True
			proxyhost=proxy.split(':')[0]
			proxyport=int(proxy.split(':')[-1])
		if useclient==None:
			x=Client(server,setproxy=useproxy,proxyhost=proxyhost,proxyport=proxyport,proxytype=proxytype,callback=th,timeout=timeout)
		else:
			x=useclient
		y=x.registernewplayer()
		callback("|9|9")
		builder=Builder(x)
		castleid=y['data']['player']['castles'][0]['id']
		quest=Quest(x,castleid)
		items=Item(x,castleid)
		items.useitem('player.box.present.2')
		builder.createbuilding(castleid,1,23)
		time.sleep(.5)
		builder.speedup(castleid,'consume.2.a',1)
		while True:
			res=x.responsehandler('server.BuildComplate',checkok=False)
			if res['data']['buildingBean']['endTime']==0.0:
				break
		quest.completequest(535)
		x.client.sendmessage('trade.newTrade',{'castleId':castleid,'price':'0.05','tradeType':0,'amount':295000,'resType':restype})
		amount=0
		idlist=[]
		while amount<300000:
			res=x.responsehandler('server.TransingTradeUpdate',checkok=False)
			tramount=res['data']['bean']['amount']
			trid=res['data']['bean']['id']
			if trid in idlist:
				continue
			idlist.append(trid)
			amount+=tramount
			if tramount>=200000:
				break
			if amount>=300000:
				tradeproblem=True
				raise
		x.client.sendmessage('trade.speedUpTrans',{'itemId':'consume.transaction.1','castleId':castleid,'transingTradeId':trid})
		res=x.responsehandler('trade.speedUpTrans')
		res=x.responsehandler('server.ResourceUpdate',checkok=False)
		x.client.sendmessage('quest.donate',{'questid': questtype, 'castleid': castleid})
		res=x.responsehandler('quest.donate')
		quest.completequest(questtype,qtype=4)
		while True:
			try:
				x.client.sendmessage("vote.voteToPlayerByName",{'name':votername})
				res=x.responsehandler('vote.voteToPlayerByName')
				break
			except Exception as e:
				if e.args[0]!=-161:
					invalidname=True
					raise
				time.sleep(1)
		callback("8|||FINISH|")
		return x
	except:
		if tradeproblem:
			return x
		try:
			x.close()
			del x
		except:
			pass
def _stvote(server,resource,votername,proxy=None,proxytype='HTTP',useclient=None,callback=None,checksource=None,timeout=30,totalrunning=None):
	x=0
	useclient=None
	while x!=None:
		if checksource!=None:
			if checksource.killsignal:
				break
		if useclient!=None:
			useclient.registered=False
		x=createacc(server,resource,votername,proxy,proxytype,useclient,callback,timeout=timeout)
		useclient=x
	totalrunning[0]-=1
def startvote(server,resource,votername,proxy=None,proxytype='HTTP',useclient=None,callback=None,checksource=None,timeout=30,totalconn=1):
	totalrunning=[0]
	for i in range(0,totalconn):
		totalrunning[0]+=1
		while True:
			try:
				Thread(target=_stvote,args=(server,resource,votername,proxy,proxytype,useclient,callback),kwargs={'checksource':checksource,'totalrunning':totalrunning,'timeout':timeout}).start()
				break
			except:
				time.sleep(.3)
	while True:
		if checksource!=None:
			if checksource.killsignal:
				if totalrunning[0]>0:
					time.sleep(.3)
					continue
				callback("|NOKILL|")
				del callback
				del totalrunning
				return
		if totalrunning[0]==0:
			callback("|KILL|")
			del callback
			del totalrunning
			return
		time.sleep(.3)