# coding=utf-8
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from myapp import db
from myapp.forms.Merchant import NewBrandForm, NewSKUForm, NewSPUForm
from myapp.models.brand import Brand
from myapp.models.goodssku import GoodsSku
from myapp.models.goodsspu import GoodsSpu

MerchantBP=Blueprint('MerchantBP',__name__)

@MerchantBP.route('/Merchant',methods=['GET'])
def Merchant():
    return render_template('Merchant.html')

@MerchantBP.route('/add_brand', methods=['GET', 'POST'])
def add_brand():
    brandForm=NewBrandForm(request.form)
    if request.method == 'POST' and brandForm.validate():
        brand=Brand()
        brand.set_attrs(brandForm.data)
        db.session.add(brand)
        db.session.commit()
        return redirect(url_for('MerchantBP.all_brand'))
    brands=Brand.query.all()
    return render_template('admin/all_brand.html',brands=brands)

@MerchantBP.route('/add_sku', methods=['GET', 'POST'])
def add_sku():
    skuForm=NewSKUForm(request.form)
    if request.method == 'POST' and skuForm.validate():
        sku=GoodsSku()
        sku.set_attrs(skuForm.data)
        db.session.add(sku)
        db.session.commit()
        return redirect(url_for('MerchantBP.all_sku'))
    sku=GoodsSku.query.all()
    return render_template('admin/all_sku.html',goodSkus=sku)

@MerchantBP.route('/add_spu', methods=['GET', 'POST'])
def add_spu():
    spuForm=NewSPUForm(request.form)
    if request.method == 'POST' and spuForm.validate():
        spu=GoodsSpu()
        spu.set_attrs(spuForm.data)
        db.session.add(spu)
        db.session.commit()
        return redirect(url_for('MerchantBP.all_spu'))
    spu=GoodsSpu.query.all()
    return render_template('admin/all_spu.html',goodSpus=spu)



