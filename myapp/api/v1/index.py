# 首页相关内容
from flask import jsonify, request
from sqlalchemy import desc
from myapp.api import apiBP
from myapp.models.brand import Brand
from myapp.models.sku import Sku
from myapp.models.sort import Sort
from myapp.utils.exception_catch import exceptionCatch
from myapp.utils.response_code import RET
from myapp.view_models.brand import BrandViewModel
from myapp.view_models.sku import SkuViewModel

ec=exceptionCatch()

@apiBP.route('/index',methods=['GET'])
def index(page=1,pageSize=20):
    ''' 根据销量排序 '''
    # 获取数据库中数据
    with ec.dataBase_exception():
        sort=Sort()
        sku=Sku()
        sorts_left = Sort.query.filter_by().all()
        sorts_top = Sort.query.filter_by(sort.fatherSort==[sorts_left[0].sortId]).all()
        skus=Sku.query.filter_by(sku.sort_id==sorts_top[0].sortId).all().limit(pageSize*(page-1),pageSize*page)
    # 将数据转换为字典
    sorts_left_list=[ sort_left.to_dict() for sort_left in sorts_left]
    sorts_top_list=[ sort_top.to_dict() for sort_top in sorts_top]
    sku_list = [SkuViewModel(sku) for sku in skus]
    return jsonify(errno=RET.OK, errmsg="OK", data={'sorts_left_list':sorts_left_list,'sorts_top_list':sorts_top_list,'sku_list':sku_list})

@apiBP.route('/sortingByRecommend',methods=['GET'])
def sortingByRecommend(page=1,pageSize=20):
    ''' 根据销量排序 '''
    # 获取数据库中数据
    with ec.dataBase_exception():
        sku=Sku()
        skus=Sku.query.order_by(desc(sku.sales)).all().limit(pageSize*(page-1),pageSize*page)
    # 将数据转换为字典
    sku_list = [SkuViewModel(sku) for sku in skus]
    return jsonify(errno=RET.OK, errmsg="OK", data={'data':sku_list})


@apiBP.route('/sortingByCreateTime',methods=['GET'])
def sortingByCreateTime(page=1,pageSize=20):
    ''' 根据创建时间倒序排序 '''
    # 获取数据库中数据
    with ec.dataBase_exception():
        sku=Sku()
        skus=Sku.query.order_by(desc(sku.create_time)).all().limit(pageSize*(page-1),pageSize*page)
    # 将数据转换为字典
    sku_list = [SkuViewModel(sku) for sku in skus]
    return jsonify(errno=RET.OK, errmsg="OK", data={'data':sku_list})


@apiBP.route('/sortingByKeyWord',methods=['GET'])
def sortingByKeyWord(page=1,pageSize=20):
    ''' 根据关键字查询 '''
    request_data=request.get_json()
    key_word=request_data.get['key_word']
    # 获取数据库中数据
    with ec.dataBase_exception():
        sku=Sku()
        skus=Sku.query.filter_by(sku.sku_name==key_word).all().limit(pageSize*(page-1),pageSize*page)
        brand=Brand()
        brands=Brand.query.filter_by(brand.brand_name==key_word).all().limit(pageSize*(page-1),pageSize*page)
    # 将数据转换为字典
    sku_list = [SkuViewModel(sku) for sku in skus]
    sku_list.append([ BrandViewModel(brand) for brand in brands])
    return jsonify(errno=RET.OK, errmsg="OK", data={'data':sku_list})






