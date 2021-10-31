class SkuViewModel:
    def __init__(self, data):
        self.name = data.skuname
        self.skufatherid = data.skufatherid
        self.declaration=data.declaration
        self.brandid = data.brandid

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


