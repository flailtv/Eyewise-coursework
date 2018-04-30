"""empty message

Revision ID: ece8f293fb04
Revises: 76c6442afb22
Create Date: 2018-04-30 09:14:29.559638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ece8f293fb04'
down_revision = '76c6442afb22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('total_cost', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cart_user_id'), 'cart', ['user_id'], unique=False)
    op.add_column('order', sa.Column('cart_id', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'order', type_='foreignkey')
    op.create_foreign_key(None, 'order', 'cart', ['cart_id'], ['id'])
    op.drop_column('order', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('order', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'order', type_='foreignkey')
    op.create_foreign_key(None, 'order', 'user', ['user_id'], ['id'])
    op.drop_column('order', 'cart_id')
    op.drop_index(op.f('ix_cart_user_id'), table_name='cart')
    op.drop_table('cart')
    # ### end Alembic commands ###
