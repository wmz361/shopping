from flask import jsonify
from sqlalchemy import desc

from myapp.models.sku import GoodsSku
from myapp.view_models.sku import SkuViewModel


class indexAPI():

    @classmethod
    def sortingByRecommend(cls):
        ''' 根据销量排序 '''
        goodsSku=GoodsSku()
        goods=GoodsSku.query.order_by(desc(goodsSku.sales)).all()
        goods1=SkuViewModel(goods)
        return jsonify(errno=200, errmsg="OK", data=goods1)

