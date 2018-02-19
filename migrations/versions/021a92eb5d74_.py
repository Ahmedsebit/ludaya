"""empty message

Revision ID: 021a92eb5d74
Revises: 37dad28f0fc3
Create Date: 2018-02-17 20:53:48.568200

"""

# revision identifiers, used by Alembic.
revision = '021a92eb5d74'
down_revision = '37dad28f0fc3'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', sa.String(length=256), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')
    # ### end Alembic commands ###