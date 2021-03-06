# coding=utf-8
from operator import or_
from flask import render_template, request, Blueprint, current_app
from myapp.models.brand import Brand
from myapp.models.sku import Sku
from myapp.view_models.brand import BrandViewModel
from myapp.view_models.sku import SkuViewModel

indexBP = Blueprint("indexBP",__name__)

@indexBP.route('/', methods=['GET'])
def index():
    brandsF = Brand.query.filter_by().all()
    brandsDicFirstLevel = BrandViewModel.brand_collection(brandsF)
    brandsS = Brand.query.filter_by().all()
    brandsDicSecendLevel = BrandViewModel.brand_collection(brandsS)
    sku = Sku.query.filter_by().all()
    goodskuDic = SkuViewModel.sku_collection(sku)
    current_app.logger.error('错误信息')
    return render_template('index/indexUnLogined.html',brandsDicFirstLevel=brandsDicFirstLevel['brands'],
                           goodssku=goodskuDic
                           , brandsDicSecendLevel=brandsDicSecendLevel['brands'])

@indexBP.route('/indexLogin', methods=['GET','POST'])
def indexLogin():
    uname=request.args.get('uname')
    brandsF = Brand.query.filter(Brand.status==1,Brand.brandfather==None).all()
    brandsDicFirstLevel = BrandViewModel.brand_collection(brandsF)
    brandsS = Brand.query.filter(Brand.brandfather == 2).all()
    brandsDicSecendLevel = BrandViewModel.brand_collection(brandsS)
    sku=Sku.query.filter(Sku.brandid==13).all()
    goodskuDic=SkuViewModel.sku_collection(sku)
    return render_template('index/index_logined.html',username=uname,brandsDicFirstLevel=brandsDicFirstLevel['brands'],goodssku=goodskuDic
                           ,brandsDicSecendLevel=brandsDicSecendLevel['brands'])

@indexBP.route('/search', methods=['GET'])
def search(keywords):
    uname = request.args.get('uname')
    brands = Brand.query.filter(or_(Brand.brandname == keywords, Brand.brandid == keywords)).all()
    brandsDic = BrandViewModel.brand_collection(brands)
    sku = Sku.query.filter(or_(Sku.skuname== keywords, Sku.skuid== keywords)).all()
    goodskuDic = SkuViewModel.sku_collection(sku)
    return render_template('index/index_logined.html', username=uname, brands=brandsDic, goodssku=goodskuDic)
