"""Adde Doctor,Patient and Department classes

Revision ID: 90214a7ba516
Revises: 
Create Date: 2024-03-20 23:24:31.105633

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90214a7ba516'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('department_name', sa.String(), nullable=True),
    sa.Column('managers_name', sa.String(), nullable=True),
    sa.Column('staffs', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('doctors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('doctor_name', sa.String(), nullable=True),
    sa.Column('speciality', sa.String(), nullable=True),
    sa.Column('license_number', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('patient_name', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('sickness', sa.String(), nullable=True),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patients')
    op.drop_table('doctors')
    op.drop_table('departments')
    # ### end Alembic commands ###