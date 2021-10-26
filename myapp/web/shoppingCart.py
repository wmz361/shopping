from flask import render_template, request, Blueprint
from flask_login import login_required


shoppingCartBP = Blueprint("shoppingCartBP",__name__)

@shoppingCartBP.route('/shoppingCart',methods=['GET'])
def shoppingCart():
    uname = request.args.get('uname')
    return render_template('shoppingCart/shoppingCart.html',username=uname)