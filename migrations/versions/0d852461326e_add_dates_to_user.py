"""Add dates to user

Revision ID: 0d852461326e
Revises: 
Create Date: 2021-12-07 19:39:58.979120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d852461326e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True, server_default=sa.text('(CURRENT_TIMESTAMP)'), server_onupdate=sa.text('(CURRENT_TIMESTAMP)')))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True, server_default=sa.text('(CURRENT_TIMESTAMP)')))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('created_at')
        batch_op.drop_column('updated_at')

    # ### end Alembic commands ###