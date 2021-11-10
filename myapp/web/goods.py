from flask import render_template, Blueprint
from myapp.models.comment import Comment
from myapp.models.spu import Spu
from myapp.view_models.comment import CommentViewModel
from myapp.view_models.spu import SpuViewModel

goodsBP = Blueprint("goodsBP",__name__)
@goodsBP.route('/goodDetail',methods=['GET'])
def index():
    return render_template('goods/goodsLogined.html')

