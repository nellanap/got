"""add score

Revision ID: e4595fc189ea
Revises: 06e37f6b8d95
Create Date: 2019-03-27 23:07:50.661341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4595fc189ea'
down_revision = '06e37f6b8d95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('score', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'score')
    # ### end Alembic commands ###
