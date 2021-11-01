from flask import render_template, Blueprint, logging

from myapp.libs.redisDealwith import Redis
from myapp.view_models.constant_data_processing import ConstantDataProcessing

testBP = Blueprint("testBP",__name__)
logger = logging.getLogger(__name__) #返回一个新的以文件名为名的logger
@testBP.route('/test',methods=['GET'])
def test001():
    try:
        Redis.write('name','wmz001哈哈哈')
        return render_template('test001.html', name=Redis.read('name'))
    except:
        logger.info("this is info")
