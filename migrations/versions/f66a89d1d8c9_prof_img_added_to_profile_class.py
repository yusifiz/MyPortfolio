"""prof img added to profile class

Revision ID: f66a89d1d8c9
Revises: 53259453ba78
Create Date: 2021-09-12 01:39:50.913403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f66a89d1d8c9'
down_revision = '53259453ba78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profile', sa.Column('prof_img', sa.String(length=150), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profile', 'prof_img')
    # ### end Alembic commands ###