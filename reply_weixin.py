import itchat
import requests
#登录微信
itchat.auto_login(hotReload=True)
path='http://www.tuling123.com/openapi/api'
def message(message):
    date={
        'key':'37515ec824ab4f059c7895c8f7e6c13e',
        'info':message,
        'userId':'robot'
    }
    try:
        r=requests.post(path,date=date).json()
        print('回复%s'%r['text'])
        return r['text']
    except:
        return  ''
@itchat.msg_register(itchat.content.TEXT)
def reply(msg):
    delattrs='明白'
    friend=itchat.search_friends('你的回复对象')
    readfriend=friend[0]
    replys=message(msg('Text'))
    if msg['FromUserName']==readfriend:
        itchat.send(delattrs or replys,toUserName=readfriend)
itchat.run()
reply()
