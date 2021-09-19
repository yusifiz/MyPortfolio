"""Profile class deleted

Revision ID: 07b1eb34a834
Revises: b9f925b47160
Create Date: 2021-09-10 01:45:22.162024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '07b1eb34a834'
down_revision = 'b9f925b47160'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('prof_name', sa.VARCHAR(length=50), nullable=True),
    sa.Column('prof_age', sa.VARCHAR(length=10), nullable=True),
    sa.Column('prof_email', sa.VARCHAR(length=100), nullable=True),
    sa.Column('prof_phone', sa.VARCHAR(length=50), nullable=True),
    sa.Column('prof_adress', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###