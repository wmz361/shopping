# coding=utf-8
from flask import render_template, request, url_for, Blueprint
from flask_login import current_user
from werkzeug.utils import redirect
from myapp import db
from myapp.forms.Merchant import NewBrandForm, NewSKUForm, NewSPUForm
from myapp.models.brand import Brand
from myapp.models.goodssku import GoodsSku
from myapp.models.goodsspu import GoodsSpu
from myapp.view_models.constant_data_processing import ConstantDataProcessing

merchantBP = Blueprint("merchantBP",__name__)
@merchantBP.route('/merchant',methods=['GET'])
def Merchant(tab='brandManager',name='审核通过的品牌'):
    itemTypes,items,itemsAttributes=ConstantDataProcessing.toMethod(tab,name)
    return render_template('admin/Merchant.html',itemTypes=itemTypes,items=items,itemsAttributes=itemsAttributes)

@merchantBP.route('/add_brand', methods=['GET', 'POST'])
def add_brand():
    brandForm=NewBrandForm(request.form)
    if request.method == 'POST' and brandForm.validate():
        with db.auto_commit():
            brand=Brand()
            brand.uid=current_user.id
            brand.set_attrs(brandForm.data)
            db.session.add(brand)
    brands=Brand.query.all()
    return redirect(url_for('merchantBP.Merchant',items=brands))

@merchantBP.route('/search_brand', methods=['GET', 'POST'])
def search_brand():
    pass

@merchantBP.route('/add_sku', methods=['GET', 'POST'])
def add_sku():
    skuForm=NewSKUForm(request.form)
    if request.method == 'POST' and skuForm.validate():
        with db.auto_commit():
            sku=GoodsSku()
            sku.uid = current_user.id
            sku.set_attrs(skuForm.data)
            db.session.add(sku)
        return redirect(url_for('MerchantBP.all_sku'))
    skus=GoodsSku.query.all()
    return redirect(url_for('merchantBP.Merchant', items=skus))

@merchantBP.route('/add_spu', methods=['GET', 'POST'])
def add_spu():
    spuForm=NewSPUForm(request.form)
    if request.method == 'POST' and spuForm.validate():
        with db.auto_commit():
            spu=GoodsSpu()
            spu.uid = current_user.id
            spu.set_attrs(spuForm.data)
            db.session.add(spu)
        return redirect(url_for('MerchantBP.all_spu'))
    spus=GoodsSpu.query.all()
    return redirect(url_for('merchantBP.Merchant', items=spus))





