class MyCollectViewModel:
    def __init__(self, data):
        self.collectid = data.collectid
        self.uid = data.uid  # 商品收藏人员
        self.spuid = data.uid  # 商品spuid