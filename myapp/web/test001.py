from flask import render_template, Blueprint

from myapp.libs.redisDealwith import Redis
from myapp.view_models.constant_data_processing import ConstantDataProcessing

testBP = Blueprint("testBP",__name__)
@testBP.route('/test',methods=['GET'])
def test001():
    Redis.write('name','wmz001哈哈哈')
    return render_template('test001.html',name=Redis.read('name'))