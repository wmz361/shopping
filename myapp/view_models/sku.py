class SkuViewModel:
    def __init__(self, data):
        self.skuname = data.skuname
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
            'skuname': data.skuname,
            'declaration': data.declaration  # 品牌宣言
        }
        return sku
