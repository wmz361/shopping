class GoodTypeViewModel:
    def __init__(self, data):
        self.sortId=data.sortId
        self.sortName = data.sortName  # 分类名称
        self.sortLogo=data.sortLogo  # 分类logo
        self.declaration = data.declaration  # 分类描述
        self.fatherSort=data.fatherSort  # 父级分类名称