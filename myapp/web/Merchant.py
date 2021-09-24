# coding=utf-8
from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from myapp import db
from myapp.models.brand import Brand
from myapp.models.goodssku import GoodsSku
from myapp.models.goodsspu import GoodsSpu
MerchantBP=Blueprint('MerchantBP',__name__)
@MerchantBP.route('/Merchant',methods=['GET'])
def Merchant():
    return render_template('Merchant.html')

@MerchantBP.route('/add_brand', methods=['GET', 'POST'])
def add_brand():
    if request.method == 'POST':
        brand=Brand()
        brand.brandname = request.form.get('brandname')
        brand.logo=request.files.get('logo')
        brand.declaration = request.form.get('declaration')
        brand.brandstory = request.form.get('brandstory')
        brand.phone_num = request.form.get('phone_num')
        brand.brandurl = request.form.get('brandurl')
        db.session.add(brand)
        db.session.commit()
        return redirect(url_for('MerchantBP.all_brand'))
    return render_template('admin/add_brand.html')

@MerchantBP.route('/all_brand')
def all_brand():
    return render_template('admin/all_brand.html')

@MerchantBP.route('/add_sku', methods=['GET', 'POST'])
def add_sku():
    if request.method == 'POST':
        sku=GoodsSku()
        sku.skuname = request.form.get('skuname')
        sku.skufatherid = request.form.get('skufatherid')
        sku.brandid = request.form.get('brandid')
        db.session.add(sku)
        db.session.commit()
        return redirect(url_for('MerchantBP.all_sku'))
    return render_template('admin/add_sku.html')

@MerchantBP.route('/all_sku')
def all_sku():
    return render_template('admin/all_sku.html')

@MerchantBP.route('/add_spu', methods=['GET', 'POST'])
def add_spu():
    if request.method == 'POST':
        spu=GoodsSpu()
        spu.spuname = request.form.get('spuname')
        spu.spupicture=request.files.get('spupicture')
        spu.skuid = request.form.get('skuid')
        spu.spudescribe = request.form.get('spudescribe')
        spu.stock = request.form.get('stock')
        spu.price = request.form.get('price')
        db.session.add(spu)
        db.session.commit()
        return redirect(url_for('MerchantBP.all_spu'))
    return render_template('admin/add_brand.html')

@MerchantBP.route('/all_spu')
def all_spu():
    return render_template('admin/all_spu.html')

