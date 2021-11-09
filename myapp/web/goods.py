from flask import render_template, Blueprint
from myapp.models.comment import Comment
from myapp.models.spu import Spu
from myapp.view_models.comment import CommentViewModel
from myapp.view_models.spu import SpuViewModel

goodsBP = Blueprint("goodsBP",__name__)
@goodsBP.route('/goodDetail',methods=['GET'])
def index():
    # spu = GoodsSpu.query.filter(GoodsSpu.spuid == spuid).all()
    # goodspuDic = SpuViewModel.spu_collection(spu)
    # comment = Comment.query.filter(Comment.spuid == spuid).all()
    # commentDic = CommentViewModel.comment_collection(comment)
    # return render_template('index/goodsLogined.html',goodspuDic=goodspuDic,commentDic=commentDic)
    return render_template('goods/goodsLogined.html')

