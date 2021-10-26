class BrandViewModel:
    def __init__(self, data):
        self.brandname = data.brandname
        self.logo = data.logo
        self.declaration = data.declaration # 品牌宣言
        self.brandstory = data.brandstory  # 品牌故事
        self.brandurl = data.brandurl  # 品牌主页url
        self.phone_num = data.phone_num

    @classmethod
    def brand_collection(cls,data,keyword=''):
        returned = {
            'brands': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returned['total'] = len(data)
            returned['brands'] = [cls.__cut_brand_data(brand) for brand in data]
        return returned

    @classmethod
    def __cut_brand_data(cls,data):
        brand={
            'brandname':data.brandname,
            'logo': data.logo,
            'declaration' : data.declaration # 品牌宣言
        }
        return brand
