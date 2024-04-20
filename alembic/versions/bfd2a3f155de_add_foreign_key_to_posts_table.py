"""add foreign-key to posts table

Revision ID: bfd2a3f155de
Revises: 2f5aa3054540
Create Date: 2024-04-19 23:31:16.898979

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bfd2a3f155de'
down_revision: Union[str, None] = '2f5aa3054540'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", "posts", "users", ["owner_id"], ["id"], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint("post_users_pk", "posts")
    op.drop_column("posts", "owner_id")
    pass
