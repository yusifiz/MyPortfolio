"""password column deleted from Contact module

Revision ID: fe676ededa92
Revises: 821a305febdb
Create Date: 2021-09-15 11:35:12.944927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe676ededa92'
down_revision = '821a305febdb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contact', 'contact_password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact', sa.Column('contact_password', sa.VARCHAR(length=100), nullable=True))
    # ### end Alembic commands ###