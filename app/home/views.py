import requests
from flask import make_response
from flask import render_template
from . import home
from app.models import Movies


@home.route('/index/')
def index():
    return render_template('home/home.html')


@home.route('/detail/', methods=['GET', 'POST'])
def detail():
    return render_template('videodetail/videodetail.html')


@home.route('/handler')
def handler():
    url = 'http://qiniu-xpc0.xpccdn.com/5a3391108e465.mp4'
    r = requests.get(url)
    # print(r)
    # with open('/Users/yuqibing/', 'wb') as f:
    #     f.write(r.content)
    response = make_response(r.content)
    # r.headers['Content-Type'] = 'video/mp4'
    return response
