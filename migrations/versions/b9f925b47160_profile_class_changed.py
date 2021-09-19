"""Profile class changed

Revision ID: b9f925b47160
Revises: a1f88a84e49e
Create Date: 2021-09-10 00:42:25.842666

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9f925b47160'
down_revision = 'a1f88a84e49e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profile', 'prof_img')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profile', sa.Column('prof_img', sa.VARCHAR(length=150), nullable=True))
    # ### end Alembic commands ###