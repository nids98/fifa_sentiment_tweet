#!/usr/bin/python
# -*- coding: utf-8 -*-

from twitter import *

api = Api(consumer_key='CBNphFBKg5ShLCNP03wd55WSl',
                      consumer_secret='LpPj967bDdUAGh1Z9SNROUMsz1fVXwdjKi8lfekHroX2kcuSuJ',
                      access_token_key='996745833071575040-hEcm4iBVohFlNCSDp1xTLTHMoYtaHD2',
                      access_token_secret='BaRdNgbQGx8qtdyMKhF9d2Wu2FSGN8vRakoQDKu4TnHZV')

f = open('applaudden.txt','a')
f1 = open('maxidapplaud.txt','r+')

q="q=%23DEN%20👏&src=typd&lang=da&result_type=recent&since=2018-01-01&count=100"

i=0

try:
	tid = f1.read()
	if len(tid)==0:
		res = api.GetSearch(raw_query=q, return_json=True)
	else:
		res = api.GetSearch(raw_query=q+"&since_id="+str(tid), return_json=True)
	temp=res["statuses"]

	while i<15:
		print "Call no:",i
		i+=1
		for t in temp:
			f.write(t['text'].encode('utf-8')+',,,'+'\n')
		maxid = temp[0]["id"]
		f1.write(str(maxid))
		tid = f1.read()
		res = api.GetSearch(raw_query=q+"&since_id="+str(tid), return_json=True)
		f1.close()
		temp=res["statuses"]
		if not temp:
			break
except Exception as e:
	print e
finally:
	f.close()
print "Successfull"
