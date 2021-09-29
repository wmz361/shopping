from flask import render_template, Blueprint
from myapp.models.comment import Comment
from myapp.models.goodsspu import GoodsSpu
from myapp.view_models.comment import CommentViewModel
from myapp.view_models.spu import SpuViewModel

goodsBP = Blueprint("goodsBP",__name__)
@goodsBP.route('/goodDetail/<spuid>',methods=['GET'])
def index(spuid):
    spu = GoodsSpu.query.filter(GoodsSpu.spuid == spuid).all()
    goodspuDic = SpuViewModel.spu_collection(spu)
    comment = Comment.query.filter(Comment.spuid == spuid).all()
    commentDic = CommentViewModel.comment_collection(comment)
    return render_template('index/goodsLogined.html',goodspuDic=goodspuDic,commentDic=commentDic)

