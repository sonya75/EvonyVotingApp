from evony import *
import time
import os
import sys
from actionfactory.builder import *
from actionfactory.quest import *
from actionfactory.items import *
restypes={'food':0,'lumber':1,'stone':2,'iron':3}
quests={'food':499,'lumber':500,'stone':501,'iron':502}
server=sys.argv[1].strip()
res=sys.argv[2].strip().lower()
votername=sys.argv[3].strip()
def createacc(server,resource,votername,useclient=None):
	global restypes,quests
	invalidname=False
	try:
		invalidres=True
		restype=restypes[resource]
		questtype=quests[resource]
		invalidres=False
		if useclient==None:
			x=Client(server)
		else:
			x=useclient
		y=x.registernewplayer()
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
		print("FINISHREPORT")
		return x
	except:
		try:
			x.close()
		except:
			pass
		if invalidres:
			print("ERRORINVALIDRES")
			return
		if invalidname:
			print("ERRORINVALIDNAME")
			return
		print("ERRORREPORT")
		return
x=createacc(server,res,votername)
if x!=None:
	while True:
		x.registered=False
		createacc(server,res,votername,useclient=x)