"""add last few columns to posts table

Revision ID: 624b8131d9fc
Revises: 4b5066754c85
Create Date: 2024-03-30 15:18:29.219416

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '624b8131d9fc'
down_revision: Union[str, None] = '4b5066754c85'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable = False, server_default = sa.text('1')),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable = False, server_default = sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created at')
    pass
