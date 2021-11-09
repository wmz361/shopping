from sqlalchemy import Column, Integer, String, SmallInteger, UnicodeText, ForeignKey
from myapp.models.base import Base

class Comment(Base):
    """ 商品评论 """

    __tablename__ = 'sp_comment'
    commentId = Column(Integer, primary_key=True)
    type=Column(SmallInteger)  # 评论类型，好评、差评、一般
    order_id=Column(Integer, ForeignKey('sp_order.orderId'))  # 被评论订单id
    comment_id = Column(Integer)  # 被评论的评论id
    from_id=Column(Integer, ForeignKey('sp_user.userid'))  # 评论人id
    content=Column(UnicodeText, nullable=False)  # 评论内容
    content_picture = Column(String(128))  # 评论的图片或视频

