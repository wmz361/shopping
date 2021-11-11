from wtforms import StringField, FileField
from wtforms.validators import ValidationError
from myapp.models.brand import Brand
from myapp.models.sku import Sku
from myapp.models.spu import Spu
from .base import DataRequired, BaseForm


class NewBrandForm(BaseForm):
    brandname = StringField(
        label='品牌名称：',  # 标签
        validators=[  # 验证方式
            DataRequired()  # 不能为空
        ]
    )
    logo = FileField('品牌logo：', validators=[DataRequired()])
    brandurl = StringField('品牌主页url：', validators=[DataRequired()])
    phone_num = StringField('品牌联系方式：', validators=[DataRequired()])


    def validate_brandname(self, field):
        """ 校验名称是否重复 """
        if Brand.query.filter_by(brandname=field.data).first():
            raise ValidationError('品牌已被注册')


class NewSKUForm(BaseForm):
    skuname = StringField(
        label='sku名称：',  # 标签
        validators=[  # 验证方式
            DataRequired()  # 不能为空
        ]
    )
    brandid = StringField('品牌id：', validators=[DataRequired()])

    def validate_skuname(self, field):
        """ 校验名称是否重复 """
        if Sku.query.filter_by(skuname=field.data).first():
            raise ValidationError('sku已被注册')


class NewSPUForm(BaseForm):
    spuname = StringField(
        label='spu名称：',  # 标签
        validators=[  # 验证方式
            DataRequired()  # 不能为空
        ]
    )
    stock = StringField('库 存：', validators=[DataRequired()])
    price = StringField('价 格：', validators=[DataRequired()])
    spupicture = FileField('图 片：', validators=[DataRequired()])

    def validate_spuname(self, field):
        """ 校验名称是否重复 """
        if Spu.query.filter_by(spuname=field.data).first():
            raise ValidationError('spu已被注册')