# -*- coding:utf-8 -*-

from flask import Flask,request,url_for
app=Flask(__name__)

@app.route('/')
def index():
    return '<h1>Home Page</h1>'

# 路由——可以使用户不访问索引页，直接访问特定页面
@app.route('/user/<username>')
def hello2user(username):
    return '<h1>Hello %s</h1>'%username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return '<h1>Post %d</h1>'%post_id

# 重定向行为/ 唯一URL ->有助于避免搜索引擎索引同一个页面两次
@app.route('/test/')                    #当访问test不带斜线的URL时，会被Flask
def test1():                            #重新定向到带斜线的规范的（test）URL
    return '<h1>URL结尾带斜线</h1>'  

@app.route('/test2')                    #这种情况访问带斜线的URL时会产生错误
def test2():                            #保证了URL的唯一
    return '<h1>URL结尾不不不带斜线了</h1>'

@app.route('/user/<username>')
def profile(username): pass


@app.route('/signin',methods=['Get'])
def show_signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


#构造URL
'''
用 url_for() 来给指定的函数构造 URL。
它接受函数名作为第一个参数，也接受对应 URL 规则的变量部分的命名参数。
未知变量部分会添加到 URL 末尾作为查询参数

为什么你要构建 URL 而非在模板中硬编码？这里有三个绝妙的理由：

1.反向构建通常比硬编码的描述性更好。
  更重要的是，它允许你一次性修改 URL， 而不是到处边找边改。
2.URL构建会转义特殊字符和Unicode数据,免去你很多麻烦。
3.如果你的应用不位于URL的根路径（比如，在/myapplication下，而不是/），
  url_for() 会妥善处理这个问题。
'''
with app.test_request_context():
    print(url_for('index'))
    print(url_for('signin', next='/'))
    print(url_for('profile', username='John Doe'))


#HTTP方法

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':      #对于同一个URL，可针对不同的http方法进行
        do_the_login()                #相应的处理
    else:
        #show_login_form()
        return '<h1>123456789</h1>'


#运行程序
if __name__ == '__main__':
    app.debug = True            #启动调试模式
    app.run(host='127.0.0.1')     #让操作系统监听所有公网IP