"""crear tabla

Revision ID: cc8a0935d169
Revises: 
Create Date: 2025-02-05 22:30:25.964605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc8a0935d169'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tarea',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=50), nullable=False),
    sa.Column('descripcion', sa.String(length=250), nullable=True),
    sa.Column('completada', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tarea')
    # ### end Alembic commands ###
