class CommentViewModel:
    def __init__(self, data):
        self.commentId=data.commentId
        self.type = data.type  # 评论类型，好评、差评、一般
        self.order_id = data.order_id  # 被评论订单id
        self.comment_id = data.comment_id  # 被评论的评论id
        self.from_id = data.from_id  # 评论人id
        self.content = data.content  # 评论内容
        self.content_picture = data.content_picture  # 评论的图片或视频