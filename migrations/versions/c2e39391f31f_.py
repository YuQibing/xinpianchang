"""empty message

Revision ID: c2e39391f31f
Revises: 
Create Date: 2017-12-18 18:21:57.724593

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2e39391f31f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=40), nullable=True),
    sa.Column('views', sa.Integer(), nullable=True),
    sa.Column('good', sa.Integer(), nullable=True),
    sa.Column('auth', sa.String(length=30), nullable=True),
    sa.Column('vocation', sa.String(length=30), nullable=True),
    sa.Column('video_url', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    # ### end Alembic commands ###