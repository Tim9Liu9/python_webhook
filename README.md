# python_webhook
  本人公司在开源中国[码云](https://gitee.com)上的webhook部署脚本，是本人采用Tornado实现的，因为公司的服务器是centos6.8，自带python2.6.6，Tornado必要要python2.7或python3环境，因此要安装起来对于没有python基础的朋友是个麻烦事情。下面2个脚本不用安装任何包，就可以在centosOS6.x、centOS7.x、ubuntu14.04、ubuntu16.04上运行，简单方便。  
  
    
#### SimpleWebHook.py : 支持python2.6、python2.7不支持python3.x
    用python2.x的SimpleHTTPServer实现的webhook自动部署脚本。可以用于码云的webhook，也可以修改成github上使用。  
- - - 
#### WebHookAll.py : 支持python2.x、python3.x （推荐使用）
    用python自带的WSGI(wsgiref)实现的webhook自动部署脚本。主要用于码云的webhook，也可以修改成github上使用。 

  
- - -  
  
### 部署步骤
===

> Python 使用 WebHookAll.py 实现 WebHook 自动部署 Git 项目

为了方便开发测试或项目部署至服务器不那么繁琐，搞一个自动部署的小轮子也是非常有必要的。

这里需要涉及到 https://gitee.com 码云 项目托管平台(也可以用 Github 平台)，Linux服务器的自带的python。

同时配置项目托管平台的个人私钥或项目公钥，保证 `git pull` 能直接拉取。  [码云官方文档](http://git.mydoc.io/?t=154711)  ; Linux记得开启请求的端口号，这里是：1010，防止防火墙的屏蔽。如果是阿里云，记得在阿里云控制台的实例的安全组里面添加入站tcp端口：1010。  

## 安装

1.下载或克隆此项目: 克隆的时候最好使用ssh协议

```shell
git clone git@github.com:Tim9Liu9/python_webhook.git
```


## 修改配置

1.修改 `WebHookAll.py` 中变量：

```python
    # 此处修改端口号
    PORT = 1010
    # 此处修改码云上设置的密码
    PASSWORD = "timliu1010"
    # git pull要更新代码的目录
    PATH = "/data/www/webhook/python_webhook/"
```


## 启动

1.运行python脚本开启后台进程运行

```shell
setsid python /data/sh/WebHookAll.py &
```

## 配置 gitee.com 项目里面 

1.`url` 填你的域名 `http://xxx.xxx.com:1010`

2.`密码` 填 `timliu1010`

## 测试

1.本地于服务器自动部署的git项目中使用 git 提交更新一下代码

```shell
touch test.md
git push 提交到服务器
```

2.查看服务器上自动部署的git项目中是否存在 `test.md`

done.
  
- - -    
  
