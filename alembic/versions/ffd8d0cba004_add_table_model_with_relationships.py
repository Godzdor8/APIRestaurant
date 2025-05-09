"""Add Table model with relationships

Revision ID: ffd8d0cba004
Revises: 99341f675db3
Create Date: 2025-04-11 12:32:49.112374

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ffd8d0cba004'
down_revision: Union[str, None] = '99341f675db3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tables', 'location',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tables', 'location',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
