class BrandViewModel:
    def __init__(self, data):
        self.brandname = data['brandname']
        self.logo = data['logo']
        self.declaration = data['declaration']  # 品牌宣言
        self.brandstory = data['brandstory']  # 品牌故事
        self.brandurl = data['brandurl']  # 品牌主页url
        self.phone_num = data['phone_num']
