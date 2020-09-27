"""empty message

Revision ID: 412ccc5e3c11
Revises: aed42d17280b
Create Date: 2020-09-27 11:32:18.551226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '412ccc5e3c11'
down_revision = 'aed42d17280b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_comment',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('body', sa.String(length=400), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('parent_id', sa.INTEGER(), nullable=True),
    sa.Column('replied_id', sa.INTEGER(), nullable=True),
    sa.Column('author_id', sa.INTEGER(), nullable=True),
    sa.Column('photo_id', sa.INTEGER(), nullable=True),
    sa.Column('delete_flag', sa.INTEGER(), nullable=True, comment='this comment delete flag 0 no 1 yes'),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['photo_id'], ['blog.id'], ),
    sa.ForeignKeyConstraint(['replied_id'], ['blog_comment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_comment')
    # ### end Alembic commands ###
