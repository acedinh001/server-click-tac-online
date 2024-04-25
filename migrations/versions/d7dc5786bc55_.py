"""empty message

Revision ID: d7dc5786bc55
Revises: 
Create Date: 2024-04-23 16:32:55.493568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7dc5786bc55'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('devices',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('device_name', sa.String(length=80), nullable=False),
    sa.Column('appium_port', sa.Integer(), nullable=False),
    sa.Column('system_port', sa.Integer(), nullable=False),
    sa.Column('key_proxy', sa.String(length=80), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('keywordcombos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_chosen', sa.Boolean(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=80), nullable=False),
    sa.Column('is_login_gmail', sa.Boolean(), nullable=False),
    sa.Column('time_search_min', sa.Integer(), nullable=False),
    sa.Column('time_search_max', sa.Integer(), nullable=False),
    sa.Column('time_onpage_min', sa.Integer(), nullable=False),
    sa.Column('time_onpage_max', sa.Integer(), nullable=False),
    sa.Column('exclude_domains', sa.String(length=80), nullable=False),
    sa.Column('ads_char', sa.String(length=80), nullable=False),
    sa.Column('proxy_name', sa.String(length=80), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('keywords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=80), nullable=False),
    sa.Column('keywordcombo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['keywordcombo_id'], ['keywordcombos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('keywords')
    op.drop_table('settings')
    op.drop_table('keywordcombos')
    op.drop_table('devices')
    op.drop_table('profiles')
    # ### end Alembic commands ###
