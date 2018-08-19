#!/usr/bin/env python
#  -*- coding:utf-8 -*-
"""
    チャットボット LINE 操作 エントリポイント
"""

from definition.config import Config
from flask import Flask, request, abort, render_template
from cores.message import messageAPI

from linebot import (LineBotApi, WebhookHandler)
from linebot.models import (MessageEvent, TextMessage,TextSendMessage,ImageSendMessage)
from linebot.exceptions import (InvalidSignatureError,LineBotApiError)

#static_url = 'https://0a8e3d6d.ngrok.io'
static_url = 'https://excpyonbot.herokuapp.com'
static_folder = 'bin'

config = Config()
mApi = messageAPI()

app = Flask(__name__, static_folder=static_folder)
line_bot_api = LineBotApi(config.token)
handler = WebhookHandler(config.secret)

@app.route("/")
def index():
    return render_template('index.html', title="hello excpyon")


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
    _response = mApi.response(event.source.sender_id,event.message.text)
    if not _response == None:
        messages = createMessage(_response)
        try:
            line_bot_api.reply_message(event.reply_token,messages)
        except LineBotApiError as e:
            print(e)


def createMessage(_response):
    _original = '/'.join([static_url,static_folder, _response.original_image])
    _preview  = '/'.join([static_url,static_folder, _response.preview_image])
    _tmp1 = TextSendMessage(text=_response.text)
    _tmp2 = ImageSendMessage(original_content_url=_original, preview_image_url=_preview)
    _messages = [_tmp1,_tmp2]
    return _messages

if __name__ == "__main__":
    app.run(threaded=True, debug=True)

"""
    while True:
        text = input('> ')
        result = mApi.response(text)
        if not result == None:
            for c in result.response():
                print(c)
"""
