class SpuViewModel:
    def __init__(self, data):
        self.spuname = data['spuname']
        self.skuid = data['skuid']
        self.spudescribe = data['spudescribe']  # 品牌描述
        self.stock = data['stock']  # 库存
        self.price = data['price']
        self.spupicture = data['spupicture']  # 图片