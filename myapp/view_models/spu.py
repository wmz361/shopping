class SpuViewModel:
    def __init__(self, data):
        self.spuname = data['spuname']
        self.skuid = data['skuid']
        self.spudescribe = data['spudescribe']  # 品牌描述
        self.stock = data['stock']  # 库存
        self.price = data['price']
        self.spupicture = data['spupicture']  # 图片

    @classmethod
    def spu_collection(cls, data, keyword=''):
        returned = {
            'spus': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = len(data)
            returned['spus'] = [cls.__cut_spu_data(spu) for spu in data]
        return returned

    @classmethod
    def __cut_spu_data(cls, data):
        spu = {
            'spuname': data.spuname,
            'spudescribe': data.spudescribe,
            'stock': data.stock,  # 品牌宣言
            'price': data.price,
            'spupicture': data.spupicture,
        }
        return spu