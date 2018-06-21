#!/usr/bin/python
# -*- coding: utf-8 -*-

from twitter import *

api = Api(consumer_key='IIxGHjK9oQNh6WtD8Jl8iNIDz',
                      consumer_secret='z4T9k4QxaMafKUiQcnewC1xoKSJhMM0nki8ItkXUXgc5hsZfyJ',
                      access_token_key='994419842726805504-m5W1ZA4hll108sKSnyEfA88axynRiWJ',
                      access_token_secret='TFloRt0np39kiXa4lHz52B01nch3FQCQjePr4LI5Im3Zg')

f = open('aus.txt','a')
f1 = open('maxidaus.txt','r+')

q="q=%23AUS&src=typd&lang=en&result_type=recent&since=2018-01-01&count=100"

i=0

try:
	tid = f1.read()
	res = api.GetSearch(raw_query=q+"&since_id="+str(tid), return_json=True)
	temp=res["statuses"]
	f1.close()

	while i<15:
		if not temp:
			break
		print "Call no:",i
		i+=1

		for t in temp:
			f.write(t['text'].encode('utf-8')+',,,'+'\n')
		maxid = temp[0]["id"]
		f1 = open('maxidaus.txt','r+')
		f1.write(str(maxid))
		tid = f1.read()
		res = api.GetSearch(raw_query=q+"&since_id="+str(tid), return_json=True)
		f1.close()
		temp=res["statuses"]
		
except Exception as e:
	print e
finally:
	f.close()
print "Successfull"
