from sqlalchemy import desc

from myapp.models.goodssku import GoodsSku


class indexAPI():

    @classmethod
    def sortingByRecommend(cls):
        ''' 根据销量排序 '''
        goodsSku=GoodsSku()
        goods=GoodsSku.query.order_by(desc(goodsSku.sales)).all()

        return goods

