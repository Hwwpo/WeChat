import hashlib
import reply
import receive
import web

from plugins.weather.data_souce import get_weather_of_city
from plugins.weather.messageget import msgget
from .plugins.weather import messageget
from jieba import posseg
class Handle(object):
    def POST(self):
        try:
            webData = web.data()
            print ("Handle Post webdata is ", webData)
            #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if msgget(recMsg.Content):
                    city = msgget(recMsg.Content)
                    content = get_weather_of_city(city)
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print ("暂且不处理")
                return "success"
        except Exception as Argment:
            return Argment