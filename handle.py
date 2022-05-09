import hashlib
import web
import reply
import receive

from plugins.weather.data_souce import get_weather_of_city
from plugins.weather.messageget import msgget
from plugins.yiqing.messageget import yiqingchaxun
class Handle(object):
	def POST(self):
		try:
			webData = web.data()
			print ("Handle Post webdata is ", webData)
            #后台打日志
			recMsg = receive.parse_xml(webData)
			if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
				print("get message successfully")
				toUser = recMsg.FromUserName
				fromUser = recMsg.ToUserName
				recMsg.Content = (recMsg.Content).decode('utf-8')
				if '天气' in recMsg.Content:
					if msgget(recMsg.Content):
						city = msgget(recMsg.Content)
						print(city)
						content = get_weather_of_city(city)
						print(content)
						replyMsg = reply.TextMsg(toUser, fromUser, content)
						return replyMsg.send()
					else:
						return "success"
				if '疫情' in recMsg.Content:
					if msgget(recMsg.Content):
						city = msgget(recMsg.Content)
						content = yiqingchaxun(city)
						replyMsg = reply.TextMsg(toUser, fromUser, content)
						return replyMsg.send()
					else:
						return "success"
			else:
				print ("暂且不处理")
				return "success"
		except Exception as Argument:
			return Argument
	def GET(self):
		try:
			data = web.input()
			if len(data) == 0:
				return "hello, this is handle view"
			signature = data.signature
			timestamp = data.timestamp
			nonce = data.nonce
			echostr = data.echostr
			token = "1422322819" #请按照公众平台官网\基本配置中信息填写

			List = [token, timestamp, nonce]
			List.sort()
			sha1 = hashlib.sha1()
			sha1.update(List[0].encode('utf-8'))
			sha1.update(List[1].encode('utf-8'))
			sha1.update(List[2].encode('utf-8'))
			hashcode = sha1.hexdigest()
			print("handle/GET func: hashcode, signature: ", hashcode, signature)
			print(type(echostr))
			if hashcode == signature:
				print('1')
				return echostr
			else:
				return ""
		except Exception as Argument:
			return Argument
