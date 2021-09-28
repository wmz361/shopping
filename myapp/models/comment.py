from sqlalchemy import Column, Integer, String, SmallInteger, UnicodeText, LargeBinary,Date
from myapp.models.base import Base

class Comment(Base):
    ''' 评论表 '''
    __tablename__ = 'comments_info'
    id = Column(Integer, primary_key=True)
    type=Column(SmallInteger)
    owner_id=Column(Integer, nullable=False)  # 被评论spuid
    comment_id = Column(Integer, nullable=False)  # 被评论的评论id
    from_id=Column(Integer, nullable=False)  # 评论人id
    like_num=Column(Integer,default=0)  # 点赞数量
    content=Column(UnicodeText)  # 评论内容
    content_picture = Column(LargeBinary)  # 评论的图片或视频

