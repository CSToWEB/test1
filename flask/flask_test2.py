# -*- coding:utf-8 -*-

from flask import Flask, render_template,url_for,Markup,request
from flask import get_flashed_messages
app=Flask(__name__)

#静态文件
#url_for('static', filename='style.css')

#模板渲染
'''
使用 render_template() 方法来渲染模板。
你需要做的一切就是将模板名和你想作为关键字的参数传入模板的变量
'''
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

'''
自动转义功能默认是开启的，所以如果 name 包含 HTML ，它将会被自动转义。
如果你能信任一个变量，并且你知道它是安全的（例如一个模块把 Wiki 标记转换为 HTML）
你可以用 Markup 类或 |safe 过滤器在模板中把它标记为安全的.
'''
# Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
# Markup.escape('<blink>hacker</blink>')
# Markup('<em>Marked up</em> &raquo; HTML').striptags()

#文件上传
# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('E:/U盘备份/3.C#/Python练习/flask/uploaded_file.txt')


#运行程序
if __name__ == '__main__':
    app.debug = True            #启动调试模式
    app.run(host='127.0.0.2')