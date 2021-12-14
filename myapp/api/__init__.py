from flask import Blueprint

apiBP=Blueprint('apiBP',__name__,template_folder='v1/templates')
from .v1 import index,login,Order,userCenter