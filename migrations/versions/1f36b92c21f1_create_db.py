"""create db

Revision ID: 1f36b92c21f1
Revises: 
Create Date: 2024-10-02 11:03:03.760687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f36b92c21f1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_create', sa.DateTime(), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('orderitem',
    sa.Column('id_order', sa.Integer(), nullable=True),
    sa.Column('id_product', sa.Integer(), nullable=True),
    sa.Column('totla', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_order'], ['order.id'], ),
    sa.ForeignKeyConstraint(['id_product'], ['product.id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orderitem')
    op.drop_table('product')
    op.drop_table('order')
    # ### end Alembic commands ###
