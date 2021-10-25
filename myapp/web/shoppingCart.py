from flask import render_template, request, url_for, Blueprint
from flask_login import login_required


shoppingCartBP = Blueprint("shoppingCartBP",__name__)

@shoppingCartBP.route('/shoppingCart/<uname>',methods=['GET'])
@login_required
def shoppingCart():
    uname = request.args.get('uname')
    return render_template('shoppingCart/shoppingCart.html',username=uname)