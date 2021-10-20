# coding=utf-8
from operator import or_
from flask import render_template, request, Blueprint
from myapp.models.brand import Brand
from myapp.models.goodssku import GoodsSku
from myapp.view_models.brand import BrandViewModel
from myapp.view_models.sku import SkuViewModel

indexBP = Blueprint("indexBP",__name__)

@indexBP.route('/', methods=['GET'])
def index():
    return render_template('index/indexUnLogined.html')

@indexBP.route('/indexLogin', methods=['GET','POST'])
def indexLogin():
    uname=request.args.get('uname')
    # brands = Brand.query.filter_by().all()
    # brandsDic = BrandViewModel.brand_collection(brands)
    # sku=GoodsSku.query.filter_by().all()
    # goodskuDic=SkuViewModel.sku_collection(sku)
    brandsDic=[{"brandname":'品牌01'}]
    goodskuDic=[{"title":"商品001","price":"100元"}]
    return render_template('index/indexLogined.html',username=uname,brands=brandsDic,goodssku=goodskuDic)

@indexBP.route('/search', methods=['GET'])
def search(keywords):
    uname = request.args.get('uname')
    brands = Brand.query.filter(or_(Brand.brandname == keywords, Brand.brandid == keywords)).all()
    brandsDic = BrandViewModel.brand_collection(brands)
    sku = GoodsSku.query.filter(or_(GoodsSku.skuname== keywords, GoodsSku.skuid== keywords)).all()
    goodskuDic = SkuViewModel.sku_collection(sku)
    return render_template('index/indexLogined.html', username=uname, brands=brandsDic, goodssku=goodskuDic)
