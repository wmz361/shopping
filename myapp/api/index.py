from sqlalchemy import desc

from myapp.models.goodssku import GoodsSku


class indexAPI():

    @classmethod
    def sortingByRecommend(cls):
        ''' 根据销量排序 '''
        goods=GoodsSku.query.order_by(desc(GoodsSku.sales)).all()
        GoodsSku.to_dict()
