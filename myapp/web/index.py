# coding=utf-8
from flask import  render_template
from myapp.web import web


@web.route('/',methods=['GET'])
def index():
    return render_template('indexUnLogined.html')
