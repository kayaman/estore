"""empty message

Revision ID: a564ee7612db
Revises:
Create Date: 2020-04-18 16:15:21.811925

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a564ee7612db'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.add_column('users', sa.Column('name', sa.String(length=80), nullable=False))
    op.create_unique_constraint(None, 'users', ['name'])
    op.drop_column('users', 'active')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('active', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'name')
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key'),
    sa.UniqueConstraint('name', name='user_name_key')
    )
    ### end Alembic commands ###
