"""empty message

Revision ID: 04d917351ec1
Revises: a4ae01a7a9a6
Create Date: 2018-03-27 16:14:12.058550

"""

# revision identifiers, used by Alembic.
revision = '04d917351ec1'
down_revision = 'a4ae01a7a9a6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('status', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'status')
    # ### end Alembic commands ###
