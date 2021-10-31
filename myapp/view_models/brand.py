class BrandViewModel:
    def __init__(self, data):
        self.name = data.brandname
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
            'name':data.brandname,
            'logo': data.logo,
            'declaration' : data.declaration # 品牌宣言
        }
        return brand

    @classmethod
    def add_brands(cls):
        brand = {
            'name':'品牌名称',
            'declaration':'品牌宣言',
            'brandid':'品牌url',
            'phone_num':'品牌联系方式'
        }
        return brand
