from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials 
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.websockets import WebSocket
from starlette.status import HTTP_401_UNAUTHORIZED 
import db
from models import User
import hashlib
from auth import auth
import datetime

import re
pattern = re.compile(r'\w{4,20}') 
pattern_mail = re.compile(r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$')  # Email

from generativeSystem import *


app = FastAPI(
    title = 'Autumn Hackathon ChatApp',
    descripstion = 'Chat app with FastAPI and starlette',
    version = '0.1 hackathon ver'
)

security = HTTPBasic()


#Template Settings(Jinja2)  テンプレ→Temple→Jinjaらしい。 だいぶ違うような……
templates = Jinja2Templates(directory='templates')
jinja_env = templates.env

def index(request: Request):
    return templates.TemplateResponse('index.html',{'request': request})

def chat(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    # Authに投げる
    username = auth(credentials)

    # userdata
    user = db.session.query(User).filter(User.username == username).first()
    db.session.close()

    # 今日の日付と来週の日付
    today = datetime.datetime.now()

    return templates.TemplateResponse('chat.html',
                                    {'request': request, 
                                    'user': user}
    )

async def register(request: Request):
    if request.method == 'GET':
        return templates.TemplateResponse('register.html',
                                        {'request': request,
                                        'user': '',
                                        'error': []}
        )
    if request.method == 'POST':
        #受け取るデータ
        data = await request.form()
        username = data.get('username')
        password = data.get('password')
        password_tmp = data.get('password_tmp')
        mail = data.get('mail')

        error = []

        tmp_user = db.session.query(User).filter(User.username == username).first()

        #エラーハンドリング 色々あるね……
        if tmp_user is not None:
            error.append('同じユーザ名のユーザが存在します。')
        if password != password_tmp:
            error.append('入力したパスワードが一致しません。')
        if pattern.match(username) is None:
            error.append('ユーザ名は4~20文字の半角英数字にしてください。')
        if pattern.match(password) is None:
            error.append('パスワードは4~20文字の半角英数字にしてください。')
        if pattern_mail.match(mail) is None:
            error.append('正しくメールアドレスを入力してください。')

        #エラー発生時に再度登録ページに戻す
        if error:
            return templates.TemplateResponse('register.html',
                                              {'request': request,
                                               'username': username,
                                               'error': error})

        #登録処理
        user = User(username, password, mail)
        db.session.add(user)
        db.session.commit()
        db.session.close()
 
        return templates.TemplateResponse('register_complete.html',
                                          {'request': request,
                                           'username': username})

async def bot_reply(sendMessage,request:Request, credentials: HTTPBasicCredentials = Depends(security)):
    bot = GenerativeSystem()
    username = auth(credentials)
    #messages.append("test")
    bot_rep = bot.reply(sendMessage)
    #data.messageText
    print("Bot reply to" + username: bot_rep)
    return bot_rep


# @app.websocket("/ws")
# async def websocket_endpoint(ws: WebSocket):
#     #user = db.session.query(User).filter(User.username == username).first()
#     #db.session.close()
#     #client = user['username']

#     print(a)
#     await ws.accept()
#     try:
#         while True:
#             data = await ws.receive_text()
#             print(data)
#     except:
#         await ws.close()


# def get(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
#     # auth
#     username = auth(credentials)

#     # userdata
#     user = db.session.query(User).filter(User.username == username).first()
#     db.session.close()

#     # JSON nageru test
#     jsondata = {
#         'username': user.username,
#         'content': 'test'
#     }

#     return jsondata
