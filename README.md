# python_webhook
  本人公司在开源中国[码云](https://gitee.com)上的webhook部署脚本，是本人采用Tornado实现的，因为公司的服务器是centos6.8，自带python2.6.6，Tornado必要要python2.7或python3环境，因此要安装起来对于没有python基础的朋友是个麻烦事情。下面2个脚本不用安装任何包，就可以在centosOS6.x、centOS7.x、ubuntu14.04、ubuntu16.04上运行，简单方便。  
  
    
#### SimpleWebHook.py : 支持python2.6、python2.7不支持python3.x
    用python2.x的SimpleHTTPServer实现的webhook自动部署脚本。可以用于码云的webhook，也可以修改成github上使用。  
- - - 
#### WebHookAll.py : 支持python2.x、python3.x （推荐使用）
    用python自带的WSGI(wsgiref)实现的webhook自动部署脚本。主要用于码云的webhook，也可以修改成github上使用。 
