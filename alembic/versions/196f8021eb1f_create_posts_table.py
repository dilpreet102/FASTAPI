"""create posts table

Revision ID: 196f8021eb1f
Revises: 
Create Date: 2024-03-30 13:31:14.480492

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '196f8021eb1f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id' , sa.Integer(), nullable = False, primary_key = True),
                    sa.Column('title', sa.String(length=255), nullable= False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
