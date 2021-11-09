"""empty message

Revision ID: e782170fdddf
Revises: d474d4302854
Create Date: 2021-11-09 13:33:15.219400

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'e782170fdddf'
down_revision = 'd474d4302854'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sp_payType',
    sa.Column('create_time', sa.Integer(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('update_time', sa.Date(), nullable=True),
    sa.Column('payTypeId', sa.Integer(), nullable=False),
    sa.Column('payType_name', sa.String(length=64), nullable=False),
    sa.Column('payType_logo', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('payTypeId')
    )
    op.create_table('sp_myCollect',
    sa.Column('create_time', sa.Integer(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('update_time', sa.Date(), nullable=True),
    sa.Column('collectId', sa.Integer(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('spuId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['spuId'], ['sp_spu.spuId'], ),
    sa.ForeignKeyConstraint(['uid'], ['sp_user.userid'], ),
    sa.PrimaryKeyConstraint('collectId')
    )
    op.create_table('sp_spuImage',
    sa.Column('create_time', sa.Integer(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('update_time', sa.Date(), nullable=True),
    sa.Column('imageId', sa.Integer(), nullable=False),
    sa.Column('image_url', sa.String(length=128), nullable=False),
    sa.Column('spuId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['spuId'], ['sp_spu.spuId'], ),
    sa.PrimaryKeyConstraint('imageId')
    )
    op.drop_table('sp_spuimage')
    op.drop_table('sp_paytype')
    op.drop_table('sp_mycollect')
    op.drop_constraint('sp_order_ibfk_3', 'sp_order', type_='foreignkey')
    op.create_foreign_key(None, 'sp_order', 'sp_payType', ['payTypeId'], ['payTypeId'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'sp_order', type_='foreignkey')
    op.create_foreign_key('sp_order_ibfk_3', 'sp_order', 'sp_paytype', ['payTypeId'], ['payTypeId'])
    op.create_table('sp_mycollect',
    sa.Column('create_time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('update_time', sa.DATE(), nullable=True),
    sa.Column('collectId', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('uid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('spuId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['spuId'], ['sp_spu.spuId'], name='sp_mycollect_ibfk_2'),
    sa.ForeignKeyConstraint(['uid'], ['sp_user.userid'], name='sp_mycollect_ibfk_1'),
    sa.PrimaryKeyConstraint('collectId'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('sp_paytype',
    sa.Column('create_time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('update_time', sa.DATE(), nullable=True),
    sa.Column('payTypeId', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('payType_name', mysql.VARCHAR(length=64), nullable=False),
    sa.Column('payType_logo', mysql.VARCHAR(length=128), nullable=False),
    sa.PrimaryKeyConstraint('payTypeId'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('sp_spuimage',
    sa.Column('create_time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('status', mysql.SMALLINT(display_width=6), autoincrement=False, nullable=True),
    sa.Column('update_time', sa.DATE(), nullable=True),
    sa.Column('imageId', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('image_url', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('spuId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['spuId'], ['sp_spu.spuId'], name='sp_spuimage_ibfk_1'),
    sa.PrimaryKeyConstraint('imageId'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('sp_spuImage')
    op.drop_table('sp_myCollect')
    op.drop_table('sp_payType')
    # ### end Alembic commands ###
