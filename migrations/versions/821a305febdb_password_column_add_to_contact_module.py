"""password column add to Contact module

Revision ID: 821a305febdb
Revises: e037d8173a54
Create Date: 2021-09-15 01:53:40.160411

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '821a305febdb'
down_revision = 'e037d8173a54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contact', sa.Column('contact_password', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contact', 'contact_password')
    # ### end Alembic commands ###