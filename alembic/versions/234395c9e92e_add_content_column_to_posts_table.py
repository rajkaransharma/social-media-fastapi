"""add content column to posts table

Revision ID: 234395c9e92e
Revises: c8c50d4ca496
Create Date: 2022-04-20 21:12:18.212480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '234395c9e92e'
down_revision = 'c8c50d4ca496'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
