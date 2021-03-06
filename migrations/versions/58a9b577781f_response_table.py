"""response table

Revision ID: 58a9b577781f
Revises: af827b587da1
Create Date: 2019-03-25 23:36:05.624783

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '58a9b577781f'
down_revision = 'af827b587da1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('response',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('response')
    # ### end Alembic commands ###
