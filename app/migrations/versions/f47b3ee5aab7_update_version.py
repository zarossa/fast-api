"""Update version

Revision ID: f47b3ee5aab7
Revises: 41480df66df8
Create Date: 2023-11-01 10:57:21.372752

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f47b3ee5aab7'
down_revision: Union[str, None] = '41480df66df8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('booking', 'room_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('booking', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('hotel', 'services',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=False)
    op.alter_column('hotel', 'image_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('room', 'hotel_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('room', 'hotel_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('hotel', 'image_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('hotel', 'services',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               nullable=True)
    op.alter_column('booking', 'customer_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('booking', 'room_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
