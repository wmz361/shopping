class SkuViewModel:
    def __init__(self, data):
        self.skuid = data.skuid
        self.skuname = data.skuname  # 商品名称
        self.brandid = data.brandid  # 所属品牌ID
        self.sortId = data.sortId  # 所属分类ID
        self.introduction = data.introduction  # 商品简介
        self.uid = data.uid  # 商品发布人员
        self.describe = data.describe # 商品描述
        self.picture = data.picture # 商品图片
        self.sales = data.sales  # 销量

    @classmethod
    def sku_collection(cls, data, keyword=''):
        returned = {
            'skus': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = len(data)
            returned['skus'] = [cls.__cut_sku_data(sku) for sku in data]
        return returned

    @classmethod
    def __cut_sku_data(cls, data):
        sku = {
            'name': data.skuname,
            'declaration': data.declaration  # 品牌宣言
        }
        return sku

    @classmethod
    def add_skus(cls):
        dataSku={}
        dataSku['name']='品类名称'
        dataSku['skufatherid']='父类skuID'
        dataSku['brandid']='所属品牌ID'
        return dataSku


