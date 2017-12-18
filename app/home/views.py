import requests
from flask import make_response
from flask import render_template
from flask import request

from . import home
from app.models import Movies


@home.route('/index/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Movies.query.paginate(page, per_page=16, error_out=False)
    movies = pagination.items
    return render_template('home/home.html', pagination=pagination, movies=movies)


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

