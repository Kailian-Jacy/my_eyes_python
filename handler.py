# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import reply
import receive
import web
class Handle(object):
	def POST(self):
		try:
			webData = web.data()
			print("Handle Post webdata is ", webData)
			#后台打日志
			recMsg = receive.parse_xml(webData)
			if isinstance(recMsg, receive.Msg):
				# Echo Server.
				if recMsg.MsgType == 'text':
					toUser = recMsg.FromUserName
					fromUser = recMsg.ToUserName
					content = recMsg.Content
					replyMsg = reply.TextMsg(toUser, fromUser, content)
					return replyMsg.send()
				# Voice translator.
				elif recMsg.MsgType == 'voice':
					toUser = recMsg.FromUserName
					fromUser = recMsg.ToUserName
					content = "received voice."
					replyMsg = reply.TextMsg(toUser, fromUser, content)
					return replyMsg.send()
				# Image describer.
				elif recMsg.MsgType == 'image':
					toUser = recMsg.FromUserName
					fromUser = recMsg.ToUserName
					content = "received image."
					replyMsg = reply.TextMsg(toUser, fromUser, content)
					# mediaId = recMsg.MediaId
					# replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
					return replyMsg.send()
			else:
				print("暂且不处理")
				return "success"
		except Exception:
			print("exception.")