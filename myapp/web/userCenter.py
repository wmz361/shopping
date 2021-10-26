# coding=utf-8
from flask import render_template, request, url_for, Blueprint


userCenterBP = Blueprint("userCenterBP",__name__)
@userCenterBP.route('/userCenter',methods=['GET'])
def userCenter():
    uname = request.args.get('uname')
    return render_template('userCenter/userCenter.html',username=uname)