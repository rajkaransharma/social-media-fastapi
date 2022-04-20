"""add few more columns to posts table

Revision ID: 8776a390ce5e
Revises: eba7f01648eb
Create Date: 2022-04-20 21:34:44.909979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8776a390ce5e'
down_revision = 'eba7f01648eb'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
