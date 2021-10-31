from myapp.models.brand import Brand
from myapp.models.goodssku import GoodsSku
from myapp.view_models.brand import BrandViewModel
from myapp.view_models.spu import SpuViewModel


class ConstantDataProcessing():
    ''' 常量数据处理 '''
    @classmethod
    def brandManager(cls,brandTypeName='审核通过的品牌'):
        ''' 品牌管理右侧分类 '''
        brandType=['审核通过的品牌','未发布品牌','已发布未审核品牌','已发布未审核通过品牌','已下架品牌','全部品牌']
        brands=[]
        if brandTypeName==brandType[0]:
            brands = Brand.query.all()
        brandsAttributes = BrandViewModel.add_brands()
        return brandType,brands,brandsAttributes
    @classmethod
    def spuManager(cls,n):
        ''' 商品管理右侧分类 '''
        skuType = ['审核通过的商品','未发布商品','已发布未审核商品','已发布未审核通过商品','已下架商品','库存不足商品','全部商品']
        skus=[]
        if n==0:
            skus = GoodsSku.query.all()
        spuAttributes = SpuViewModel.add_spus()
        return skuType,skus,spuAttributes
    @classmethod
    def orderManager(cls):
        ''' 订单管理右侧分类 '''
        orderType = ['未发货订单','已收货订单','已评价订单','退款中订单','待收货订单','拒绝退款订单','已发货未收货订单','全部订单']
        return orderType

    @classmethod
    def brandDataAnalysis(cls):
        ''' 品牌数据分析右侧分类 '''
        brandType = ['']
        return brandType

    @classmethod
    def spuDataAnalysis(cls):
        ''' 产品数据分析品牌右侧分类 '''
        spuType = ['上货情况','下架情况','新品']
        return spuType

    @classmethod
    def orderAnalysis(cls):
        ''' 订单数据分析品牌右侧分类 '''
        orderType = ['成交情况','退货情况','库存情况','评论情况','同品类占比']
        return orderType

    @classmethod
    def toMethod(cls,data,name):
        return getattr(cls,data)()

