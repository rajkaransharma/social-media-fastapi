"""create posts table

Revision ID: c8c50d4ca496
Revises: 
Create Date: 2022-04-20 20:58:39.384760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8c50d4ca496'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                     primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    pass
