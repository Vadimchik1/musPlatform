"""add_song

Revision ID: 3c9fab0e30c4
Revises: c61c96eeddf3
Create Date: 2020-12-02 20:21:35.822440

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c9fab0e30c4'
down_revision = 'c61c96eeddf3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('song', sa.Column('song_url', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('song', 'song_url')
    # ### end Alembic commands ###
