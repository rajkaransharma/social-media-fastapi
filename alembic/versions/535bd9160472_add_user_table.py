"""add user table

Revision ID: 535bd9160472
Revises: 234395c9e92e
Create Date: 2022-04-20 21:21:05.401197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '535bd9160472'
down_revision = '234395c9e92e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
