class SpuViewModel:
    def __init__(self, data):
        self.name = data['spuname']
        self.skuid = data['skuid']
        self.spudescribe = data['spudescribe']  # 品牌描述
        self.stock = data['stock']  # 库存
        self.price = data['price']
        self.spupicture = data['spupicture']  # 图片
        self.isDefult=data.isDefult  # 是否是默认spu
        self.spuid = data.spuid


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
            'name': data.spuname,
            'spudescribe': data.spudescribe,
            'stock': data.stock,
            'price': data.price,
            'spupicture': data.spupicture,
        }
        return spu

    @classmethod
    def add_spus(cls):
        spu = {
            'name': '商品名称',
            'spudescribe': '商品描述',
            'stock': '商品库存',
            'price': '商品价格'
        }
        return spu