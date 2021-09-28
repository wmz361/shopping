# coding=utf-8
from operator import or_
from flask import render_template, request
from myapp.models.brand import Brand
from myapp.models.goodssku import GoodsSku
from myapp.view_models.brand import BrandViewModel
from myapp.view_models.sku import SkuViewModel
from myapp.web import web


@web.route('/',methods=['GET'])
def index():
    web.logger.error('this is a error')
    return render_template('index/indexUnLogined.html')

@web.route('/indexLogin/?', methods=['GET'])
def indexLogin():
    uname=request.args.get('uname')
    brands = Brand.query.filter_by().all()
    brandsDic = BrandViewModel.brand_collection(brands)
    sku=GoodsSku.query.filter_by().all()
    goodskuDic=SkuViewModel.sku_collection(sku)
    return render_template('index/indexLogined1.html',username=uname,brands=brandsDic,goodssku=goodskuDic)

@web.route('/search/?', methods=['GET'])
def indexLogin(keywords):
    uname = request.args.get('uname')
    brands = Brand.query.filter(or_(Brand.brandname == keywords, Brand.brandid == keywords)).all()
    brandsDic = BrandViewModel.brand_collection(brands)
    sku = GoodsSku.query.filter(or_(GoodsSku.skuname== keywords, GoodsSku.skuid== keywords)).all()
    goodskuDic = SkuViewModel.sku_collection(sku)
    return render_template('index/indexLogined1.html', username=uname, brands=brandsDic, goodssku=goodskuDic)
