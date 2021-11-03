class OrderViewModel:
    def __init__(self, data):
        self.orderId = data.orderId
        self.spuId = data.spuId  # spuId
        self.spuCount = data.spuCount # spu的数量
        self.addressId = data.addressId  # 收货地址id
        self.payTypeId = data.payTypeId # 支付方式id
        self.userId = data.userId  # 用户id