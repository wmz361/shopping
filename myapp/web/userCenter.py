# coding=utf-8
from flask import render_template, request, url_for, Blueprint
from flask_login import login_required,current_user
from werkzeug.utils import redirect
from myapp import db
from myapp.forms.Merchant import NewBrandForm, NewSKUForm, NewSPUForm
from myapp.models.brand import Brand
from myapp.models.goodssku import GoodsSku
from myapp.models.goodsspu import GoodsSpu


userCenterBP = Blueprint("userCenterBP",__name__)
@userCenterBP.route('/userCenter/<uname>',methods=['GET'])
@login_required
def userCenter(uname):
    return render_template('userCenter/userCenter.html',username=uname)