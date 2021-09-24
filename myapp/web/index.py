# coding=utf-8
from flask import  render_template, request, redirect, url_for, flash
# from flask_login import login_required

from myapp.forms.register import RegisterForm, LoginForm
from myapp.models.base import db
from myapp.models.user import User

from flask import Blueprint

indexBP=Blueprint('indexBP',__name__)

@indexBP.route('/',methods=['GET'])
def index():
    return render_template('indexUnLogined.html')
