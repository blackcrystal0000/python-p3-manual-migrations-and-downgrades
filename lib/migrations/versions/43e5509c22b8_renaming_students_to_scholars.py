"""Renaming students to scholars

Revision ID: 43e5509c22b8
Revises: 791279dd0760
Create Date: 2023-09-09 12:03:47.499297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43e5509c22b8'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
