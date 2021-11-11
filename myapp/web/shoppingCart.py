from flask import render_template, request, Blueprint
from flask_login import login_required


shoppingCartBP = Blueprint("shoppingCartBP",__name__)

@shoppingCartBP.route('/Order',methods=['GET'])
def shoppingCart():
    uname = request.args.get('uname')
    return render_template('Order/Order.html',username=uname)