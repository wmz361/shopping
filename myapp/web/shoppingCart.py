from flask import render_template, request, url_for, Blueprint
from flask_login import login_required,current_user
from werkzeug.utils import redirect
from myapp import db
from myapp.forms.Merchant import NewBrandForm, NewSKUForm, NewSPUForm
from myapp.models.brand import Brand
from myapp.models.goodssku import GoodsSku
from myapp.models.goodsspu import GoodsSpu


shoppingCartBP = Blueprint("shoppingCartBP",__name__)

@shoppingCartBP.route('/shoppingCart/<uname>',methods=['GET'])
@login_required
def shoppingCart(uname):
    return render_template('shoppingCart/shoppingCart.html',username=uname)