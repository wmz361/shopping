class AdressViewModel:
    def __init__(self, data):
        self.addressId=data.addressId
        self.userId=data.userId  # 创建人id
        self.provinceId=data.provinceId  # 省ID
        self.cityId=data.cityId  # 市ID
        self.districtId=data.districtId  # 区ID
        self.name=data.name  # 收货人姓名
        self.tag=data.tag  # 标签
        self.isDefult=data.isDefult # 是否为默认地址
        self.mobile=data.mobile  # 收货人手机号
        self.remark=data.remark  # 详细地址