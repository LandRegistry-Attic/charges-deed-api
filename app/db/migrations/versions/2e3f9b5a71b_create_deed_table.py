# flake8: noqa
"""create deed table

Revision ID: 2e3f9b5a71b
Revises: None
Create Date: 2015-06-30 12:31:47.933572

"""

# revision identifiers, used by Alembic.
revision = '2e3f9b5a71b'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSON


def upgrade():
    op.create_table('deed',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('json_doc', JSON, nullable=False),
                    sa.PrimaryKeyConstraint('id'))


def downgrade():
    op.drop_table('deed')
