# -*- coding:utf-8 -*-
#导入需要用到的包
from flask import Flask,request
from flask import make_response,redirect
app = Flask(__name__)

#配置根目录信息
@app.route('/')
def index():
  #在浏览器界面显示Hello World
	return 'Hello World'

#配置子目录信息
@app.route('/browser')
def browserMessage():
  #获取浏览器的头
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is %s</p>'%user_agent

#可以把地址栏的参数实例到下文中
@app.route('/user/<name>')
def user(name):
	return 'Hello %s'%name

@app.route('/cookie')
def cookieMessage():
	response = make_response('<h1>This document carries a cookie</h1>')
	response.set_cookie('answer','42')
	return response

#地址重定向
@app.route('/turn')
def testTure():
	return redirect('http://www.baidu.com')

if __name__ == '__main__':
  #服务器开启
	app.run(debug=True)
