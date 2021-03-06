"""log bool column added.

Revision ID: 16fbe3cc0d9f
Revises: ed7d5771d0e4
Create Date: 2021-09-18 03:41:26.451536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16fbe3cc0d9f'
down_revision = 'ed7d5771d0e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('login', sa.Column('log_bool', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('login', 'log_bool')
    # ### end Alembic commands ###
