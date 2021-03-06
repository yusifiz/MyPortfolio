"""date column add to blogs module

Revision ID: 2d5d762c96eb
Revises: bb91e6a9a8cd
Create Date: 2021-09-14 02:04:41.153956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d5d762c96eb'
down_revision = 'bb91e6a9a8cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'date')
    # ### end Alembic commands ###
