"""updated fields in tables

Revision ID: 723585279508
Revises: 72fa00aee736
Create Date: 2024-02-27 23:09:42.382549

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '723585279508'
down_revision: Union[str, None] = '72fa00aee736'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('grades', 'student_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('grades', 'subject_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('groups', 'name',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
    op.alter_column('students', 'first_name',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('students', 'last_name',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('students', 'group_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('subjects', 'name',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('teachers', 'first_name',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.alter_column('teachers', 'last_name',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('teachers', 'last_name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('teachers', 'first_name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('subjects', 'name',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('students', 'group_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('students', 'last_name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('students', 'first_name',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('groups', 'name',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
    op.alter_column('grades', 'subject_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('grades', 'student_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
