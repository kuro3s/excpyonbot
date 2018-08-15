#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット LINE 操作 エントリポイント
"""
import os
from cores.message import messageAPI
from definition.config import Config
from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage,TextSendMessage,ImageSendMessage)
from linebot.exceptions import LineBotApiError

config = Config()
mApi = messageAPI()

app = Flask(__name__, static_folder='bin')

line_bot_api = LineBotApi(config.token)
handler = WebhookHandler(config.secret)
#static_url = 'https://ae970c9a.ngrok.io'
static_url = 'https://excpyonbot.herokuapp.com'

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    _response = mApi.response(event.message.text)
    if not _response.text == None:
        messages = createMessage(_response)
        try:
            line_bot_api.reply_message(event.reply_token,messages)
        except LineBotApiError as e:
            print(e)


def createMessage(_response):
    _original = static_url+'/bin/'+_response.original_image
    _preview = static_url+'/bin/'+_response.preview_image
    _message1 = TextSendMessage(text=_response.text)
    _message2 = ImageSendMessage(original_content_url=_original, preview_image_url=_preview)
    _messages = [_message1,_message2]
    return _messages

if __name__ == "__main__":
    print(app.url_map)
    app.run()

    #while True:
        #text = input('> ')
        #result = message.response(text)
        #if not result.text == None:
        #            for c in result.response():
        #                print(c)
