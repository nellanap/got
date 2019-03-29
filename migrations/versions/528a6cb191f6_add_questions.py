"""add questions

Revision ID: 528a6cb191f6
Revises: 96d83237dd53
Create Date: 2019-03-26 21:30:07.117155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '528a6cb191f6'
down_revision = '96d83237dd53'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('response', sa.Column('q1', sa.String(length=64), nullable=True))
    op.add_column('response', sa.Column('q2', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('response', 'q2')
    op.drop_column('response', 'q1')
    # ### end Alembic commands ###