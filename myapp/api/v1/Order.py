# 购物车相关内容
from flask import jsonify, request
from myapp.api import apiBP
from myapp.models.base import db
from myapp.models.order import Order
from myapp.models.spu import Spu
from myapp.utils.exception_catch import exceptionCatch
from myapp.utils.response_code import RET
from myapp.view_models.order import OrderViewModel

ec=exceptionCatch()

@apiBP.route('/getOrderList/status/<userID>', methods=['GET'])
def getOrderList(status,userID,page=1,pageSize=20):
    """ 获取订单列表 """
    # 获取数据库中数据
    with ec.dataBase_exception():
        order = Order()
        orders = Order.query.filter_by(order.userId==userID,order.status==status).all().limit(pageSize * (page - 1), pageSize * page)
    # 将数据转换为字典
    orderInf_list = [OrderViewModel(order) for order in orders]
    return jsonify(errno=RET.OK, errmsg="OK", data={'data': orderInf_list})

@apiBP.route('/addToTheCart', methods=['POST'])
def addToTheCart():
    """ 加入购物车 """
    request_data=request.get_json()

@apiBP.route('/placeOrder', methods=['POST'])
def placeOrder():
    """ 下单 """
    request_data=request.get_json()
    # 新建订单
    if request_data['spu_count']>0:
        with ec.dataBase_exception():
            spu = Spu()
            spuFirst = Order.query.filter_by(spu.spuId == request_data['spuId']).first()
            with ec.dataBase_exception():
                with db.auto_commit():
                    order = Order()
                    order.set_attrs(request_data.data)
                    db.session.add(order)
        return jsonify(errno=RET.OK, errmsg="OK", data={'order': order.orderId,'spu':spuFirst})

@apiBP.route('/payment', methods=['POST'])
def payment():
    """ 付款 """
    request_data = request.get_json()
    with ec.dataBase_exception():
        success=Order.reset_status(request_data['orderId'],2)
        if success:
            return jsonify(errno=RET.OK, errmsg="OK", data={'orderId':Order.orderId})
        else:
            return jsonify(errno=RET.PARAMERR, errmsg="付款失败", data={'orderId':Order.orderId})

@apiBP.route('/ship', methods=['POST'])
def ship():
    """ 发货 """
    request_data = request.get_json()
    with ec.dataBase_exception():
        success = Order.reset_status(request_data['orderId'], 3)
        if success:
            return jsonify(errno=RET.OK, errmsg="OK", data={'orderId': Order.orderId})
        else:
            return jsonify(errno=RET.PARAMERR, errmsg="付款失败", data={'orderId': Order.orderId})

@apiBP.route('/receipt', methods=['POST'])
def receipt():
    """ 收货 """
    request_data = request.get_json()
    with ec.dataBase_exception():
        success = Order.reset_status(request_data['orderId'], 4)
        if success:
            return jsonify(errno=RET.OK, errmsg="OK", data={'orderId': Order.orderId})
        else:
            return jsonify(errno=RET.PARAMERR, errmsg="付款失败", data={'orderId': Order.orderId})

@apiBP.route('/returnTheGoods', methods=['POST'])
def returnTheGoods():
    """ 退货 """
    request_data = request.get_json()
    with ec.dataBase_exception():
        success = Order.reset_status(request_data['orderId'], 5)
        if success:
            return jsonify(errno=RET.OK, errmsg="OK", data={'orderId': Order.orderId})
        else:
            return jsonify(errno=RET.PARAMERR, errmsg="付款失败", data={'orderId': Order.orderId})

@apiBP.route('/evaluation', methods=['POST'])
def evaluation():
    """ 评价 """
    request_data = request.get_json()
    with ec.dataBase_exception():
        success = Order.reset_status(request_data['orderId'], 6)
        if success:
            return jsonify(errno=RET.OK, errmsg="OK", data={'orderId': Order.orderId})
        else:
            return jsonify(errno=RET.PARAMERR, errmsg="付款失败", data={'orderId': Order.orderId})


