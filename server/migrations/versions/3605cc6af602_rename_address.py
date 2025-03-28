"""rename address

Revision ID: 3605cc6af602
Revises: efe64c096d08
Create Date: 2025-03-25 23:47:39.835900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3605cc6af602'
down_revision = 'efe64c096d08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###