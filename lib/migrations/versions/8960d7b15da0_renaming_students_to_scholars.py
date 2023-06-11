"""Renaming students to scholars

Revision ID: 8960d7b15da0
Revises: 791279dd0760
Create Date: 2023-06-11 22:39:25.747723

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8960d7b15da0'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
