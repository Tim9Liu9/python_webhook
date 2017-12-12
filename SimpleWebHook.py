#!/usr/bin/env python
#encoding=utf-8
__author__ = 'Tim Liu'
__date__ = '2017/12/10 3:03'

import SimpleHTTPServer
import SocketServer
import json
import threading
import urlparse
import os


class ServerHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    @classmethod
    def setPassword(self, password=''):
        self.password = password

    @classmethod
    def setGitPath(self, path='/'):
        self.gitpath = path

    def targget_thread(self, post):
        # json_str = post.rfile.readline() : 读取出来的数据有问题, 而且在主线程执行，在本人的阿里云主机里面读出来要15秒样子
        parsed_path = urlparse.urlparse(self.path)
        length = self.headers.getheader('content-length');
        nbytes = int(length)
        json_str = self.rfile.read(nbytes)
        print(json_str)
        dic = {}
        try:
            dic = json.loads(json_str)
        except Exception as e:
            print(Exception,":",e)
        # 码云文档： http://git.mydoc.io/?t=154711 Push 的数据格式
        password = dic.get('password')
        if password == self.password :
            print("Password is ok! do somethings")
            # os.system("cd /data/www/webhook/python_webhook/") 这个是不会起作用的
            os.chdir(self.gitpath)
            os.system("git pull")
        else:
            print("Password is wrong!")



    def do_GET(self):
        print('do_GET')
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Don't get")
        # 阻止显示目录
        # SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
	    print('do_GET')
        t = threading.Thread(target=self.targget_thread, args=(self,))
        t.setDaemon(True)
        t.start()
        self.send_response(200)
        self.end_headers()
        self.wfile.write("success")




# 此程序只能运行在python2.x 环境，python3.x环境请勿使用！
if __name__ == '__main__':

    # 此处修改端口号
    PORT = 1010
    # 此处修改码云上设置的密码
    PASSWORD = "timliu1010"
    # git pull要更新代码的目录
    PATH = "/data/www/webhook/python_webhook/"

    Handler = ServerHandler
    Handler.setPassword(PASSWORD)
    Handler.setGitPath(PATH)
    httpd = SocketServer.TCPServer(("", PORT), Handler)
    print("service at port:{}".format(PORT))
    httpd.serve_forever()
