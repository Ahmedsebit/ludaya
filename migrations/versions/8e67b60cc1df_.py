"""empty message

Revision ID: 8e67b60cc1df
Revises: None
Create Date: 2018-03-03 10:28:54.177067

"""

# revision identifiers, used by Alembic.
revision = '8e67b60cc1df'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('current_members', sa.Integer(), nullable=True),
    sa.Column('team_lead', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('results',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('result_all', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('result_no_stop_words', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('taskgroup', sa.String(), nullable=True),
    sa.Column('taskname', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=256), nullable=False),
    sa.Column('lastname', sa.String(length=256), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('group', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('assignedtasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=2000), nullable=True),
    sa.Column('group', sa.String(length=1000), nullable=True),
    sa.Column('category', sa.String(length=1000), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('date_opened', sa.DateTime(), nullable=True),
    sa.Column('date_resolved', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(length=255), nullable=True),
    sa.Column('satisfaction', sa.Integer(), nullable=True),
    sa.Column('user_answer', sa.String(length=2000), nullable=True),
    sa.Column('evaluate_id', sa.Integer(), nullable=True),
    sa.Column('evaluate_comment', sa.String(length=2000), nullable=True),
    sa.Column('evaluated_status', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('assignedtasks')
    op.drop_table('users')
    op.drop_table('tasks')
    op.drop_table('results')
    op.drop_table('groups')
    # ### end Alembic commands ###
