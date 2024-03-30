"""add content column to posts table

Revision ID: eec5b1751ba3
Revises: 196f8021eb1f
Create Date: 2024-03-30 14:05:05.997997

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eec5b1751ba3'
down_revision: Union[str, None] = '196f8021eb1f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(length=255) , nullable =False))

    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
