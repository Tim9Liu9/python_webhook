#!/usr/bin/env python
#encoding=utf-8
__author__ = 'Tim Liu'
__date__ = '2017/12/11 10:09'

#!/usr/bin/env python
#encoding=utf-8
__author__ = 'Tim Liu'
__date__ = '2017/12/10 3:03'

from wsgiref.simple_server import make_server, WSGIRequestHandler
import json
import threading
import time
import os



class App():

    def __init__(self, gitpath='/', password=''):
        self.gitpath = gitpath
        self.password = password

    def application(self, environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])
        request_type = environ['REQUEST_METHOD']
        if request_type == 'POST':
            t = threading.Thread(target=self.targget_thread, args=(environ,))
            # t.setDaemon(True)
            t.start()
            return [b'success, webhook!']
        else:
            return [b"Don't get!"]

    # 网络请求在多线程里面处理
    def targget_thread(self, environ):
        request_body_size = 0
        try:
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        except (ValueError):
           print(" It's not json !")
        wsgi_input = environ['wsgi.input']
        print(wsgi_input)
        json_str = wsgi_input.read(request_body_size)
        print(json_str)
        dic = {}
        try:
            # python3.x里面必须要对byte字节解码，python2.x默认是string类型的字符串
            if type(json_str) != 'str':
                json_str = json_str.decode('utf-8')
            dic = json.loads(json_str)
        except Exception as e:
            print(Exception,":",e)
        # 码云文档： http://git.mydoc.io/?t=154711 Push 的数据格式
        password = dic.get('password')
        print(password)
        if password == self.password :
            print("password is ok! do somethings")
            # os.system("cd /data/www/webhook/python_webhook/") 这个是不会起作用的
            os.chdir(self.gitpath)
            os.system("git pull")
        else:
            print("Password is wrong!")

        end = time.time()




# 此程序可以在python2.x(2.6、2.7) 、python3.x环境使用！
if __name__ == '__main__':

    # 此处修改端口号
    PORT = 1010
    # 此处修改码云上设置的密码
    PASSWORD = "timliu1010"
    # git pull要更新代码的目录
    PATH = "/data/www/webhook/python_webhook/"

    app = App(PATH, PASSWORD)
    httpd = make_server('', PORT, app.application )


    print("service at port:{}".format(PORT))

    # 开始监听HTTP请求:
    httpd.serve_forever()
