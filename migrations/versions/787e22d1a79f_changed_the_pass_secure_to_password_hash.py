"""changed the pass_secure to password_hash

Revision ID: 787e22d1a79f
Revises: 27fc2af3e028
Create Date: 2020-09-28 02:48:27.253215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '787e22d1a79f'
down_revision = '27fc2af3e028'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=255), nullable=True))
    op.drop_column('users', 'pass_secure')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('pass_secure', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###