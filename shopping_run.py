from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from myapp import create_app
from myapp.models.base import db
from myapp.models.address import Address
from myapp.models.brand import Brand
from myapp.models.comment import Comment
from myapp.models.myCollect import MyCollect
from myapp.models.order import Order
from myapp.models.payType import payType
from myapp.models.sku import Sku
from myapp.models.spu import Spu
from myapp.models.sort import Sort
from myapp.models.spuImage import SpuImage
from myapp.models.user import User

app = create_app()

manager=Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)

if __name__=="__main__":
    # manager.run()
    app.run()