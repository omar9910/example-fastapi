"""add content column

Revision ID: c3d224a636ae
Revises: aa894788e0e9
Create Date: 2024-04-19 22:16:50.338327

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c3d224a636ae'
down_revision: Union[str, None] = 'aa894788e0e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
