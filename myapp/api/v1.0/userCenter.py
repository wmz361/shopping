# 用户中心相关内容
from flask import jsonify
from myapp.api import apiBP
from myapp.forms.register import RegisterForm
from myapp.models.address import Address
from myapp.models.base import db
from myapp.models.myCollect import MyCollect
from myapp.models.user import User
from myapp.utils.exception_catch import exceptionCatch
from myapp.utils.response_code import RET
from myapp.view_models.adress import AdressViewModel
from myapp.view_models.myCollect import MyCollectViewModel
from myapp.view_models.user import UserViewModel

ec=exceptionCatch()

@apiBP.route('/getUserInf/<userID>', methods=['GET'])
def getUserInf(userID,page=1,pageSize=20):
    """ 获取用户信息 """
    # 获取数据库中数据
    with ec.dataBase_exception():
        user = User()
        users = User.query.filter_by(user.userId==userID).all().limit(pageSize * (page - 1), pageSize * page)
    # 将数据转换为字典
    userInf = [UserViewModel(user) for user in users]
    return jsonify(errno=RET.OK, errmsg="OK", data={'data': userInf})

@apiBP.route('/getAllAddress/<userID>', methods=['GET'])
def getAllAddress(userID,page=1,pageSize=20):
    """ 获取所有地址 """
    # 获取数据库中数据
    with ec.dataBase_exception():
        address = Address()
        addresses = Address.query.filter_by(address.userId==userID).all().limit(pageSize * (page - 1), pageSize * page)
    # 将数据转换为字典
    address_list = [AdressViewModel(address) for address in addresses]
    return jsonify(errno=RET.OK, errmsg="OK", data={'data': address_list})

@apiBP.route('/getAllPayType/<userID>', methods=['GET'])
def getAllPayType(userID,page=1,pageSize=20):
    """ 获取所有支付方式 """
    # 获取数据库中数据
    with ec.dataBase_exception():
        address = Address()
        addresses = Address.query.filter_by(address.userId==userID).all().limit(pageSize * (page - 1), pageSize * page)
    # 将数据转换为字典
    address_list = [AdressViewModel(address) for address in addresses]
    return jsonify(errno=RET.OK, errmsg="OK", data={'data': address_list})

@apiBP.route('/getAllCollect/<userID>', methods=['GET'])
def getAllCollect(userID,page=1,pageSize=20):
    """ 获取所有收藏内容 """
    # 获取数据库中数据
    with ec.dataBase_exception():
        collect = MyCollect()
        collects = MyCollect.query.filter_by(collect.userId==userID).all().limit(pageSize * (page - 1), pageSize * page)
    # 将数据转换为字典
    collect_list = [MyCollectViewModel(collect) for collect in collects]
    return jsonify(errno=RET.OK, errmsg="OK", data={'data': collect_list})

@apiBP.route('/userInf', methods=['POST'])
def userInf():
    """ 用户信息修改 """
    personalInfForm = RegisterForm()
    if personalInfForm.validate():
        with ec.dataBase_exception():
            with db.auto_commit():
                user = User()
                user.set_attrs(personalInfForm.data)
                db.session.add(user)
        return jsonify(errno=RET.OK, errmsg="OK", data={'userId':user.userid})

@apiBP.route('/addAddress', methods=['POST'])
def addAddress():
    """ 添加地址 """
    personalInfForm = RegisterForm()
    if personalInfForm.validate():
        with ec.dataBase_exception():
            with db.auto_commit():
                user = User()
                user.set_attrs(personalInfForm.data)
                db.session.add(user)
        return jsonify(errno=RET.OK, errmsg="OK", data={'userId':user.userid})







