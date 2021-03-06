"""empty message

Revision ID: 037f1525d2b3
Revises: 20e161bf78a2
Create Date: 2021-11-06 14:19:10.977222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '037f1525d2b3'
down_revision = '20e161bf78a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todos', 'todolist', ['list_id'], ['id'])
    op.execute("insert into todolist (name) values ('unassigned');")
    op.execute('update todos set list_id = 1 where list_id is null')
    op.alter_column('todos', 'list_id', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'list_id')
    op.drop_table('todolist')
    # ### end Alembic commands ###
