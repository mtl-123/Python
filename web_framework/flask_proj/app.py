# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, url_for, flash,  redirect

'''
函数库详解：
Flask：
render_template：渲染模板函数
request：用来获取表单中的请求信息的
url_for：根据函数名，反向获取
flash：获取提示语，例如登录失败的提示
redirect：页面重定向，用来跳转页面的
'''
# 初始化一个程序实例
app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1> Hello Web Flask! </h1>'


@app.route('/user/<name>')
def index(name):
    # %s: 是填充字符串类型
    return '<h2>Hello, %s!</h2>' % name


# 主函数
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
