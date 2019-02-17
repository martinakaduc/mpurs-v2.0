import utils
import constant
import numpy as np
from aiohttp import web
import socketio
import os

sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)

@sio.on('timeElapsed', namespace='/home')
async def timeElapsed():
    """Example of how to send server generated events to clients."""
    second = 0
    minute = 0
    hour = 0
    while True:
        await sio.sleep(1)
        second += 1
        if second == 60:
            second = 0
            minute += 1
            if minute == 60:
                minute = 0
                hour += 1
        await sio.emit('timeElapsed', {'data': '%s : %s : %s' % (hour, minute, second)}, namespace='/home')

@sio.on('predictAndRecommend', namespace='/home')
async def predictAndRecommend(sid, mark):
    # print(mark)
    markDict = utils.predictMark(mark)
    # print(markDict)
    await sio.emit('markResult', markDict, room=sid, namespace='/home')
    subjectCombinationMark = utils.calculateSubjectCombinationMark(markDict)
    # print(subjectCombinationMark)
    await sio.emit('markPerGradeResult', subjectCombinationMark, room=sid, namespace='/home')
    listUniversities = utils.findUniversities(subjectCombinationMark)
    await sio.emit('universitiesResult', listUniversities, room=sid, namespace='/home')
    # for university in listUniversities:
    #     print(university)

async def mainPage(request):
    with open(constant.MAINPAGE_HTML, encoding='utf8') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.on('connect', namespace='/home')
async def connect(sid, environ):
    print('Client Connected: ' +str(sid))

@sio.on('disconnect', namespace='/home')
def disconnect(sid):
    print('Client Disconnected: ' + str(sid))

app.router.add_static('/static', constant.WEB_DIR + 'static')
app.router.add_get('/', mainPage)

if __name__ == '__main__':
    #http://0.0.0.0:8080/result?subCom=nature&math0=0&math1=0&math2=0&literature0=0&literature1=0&literature2=0&english0=0&english1=0&english2=0&physics0=0&physics1=0&physics2=0&chemistry0=0&chemistry1=0&chemistry2=0&biology0=0&biology1=0&biology2=0&history0=0&history1=0&history2=0&geography0=0&geography1=0&geography2=0&civiceducation0=0&civiceducation1=0&civiceducation2=0
    sio.start_background_task(timeElapsed)
    web.run_app(app)
