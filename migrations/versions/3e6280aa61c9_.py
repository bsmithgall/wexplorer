"""empty message

Revision ID: 3e6280aa61c9
Revises: None
Create Date: 2015-01-15 18:20:35.546802

"""

# revision identifiers, used by Alembic.
revision = '3e6280aa61c9'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('first_name', sa.String(length=30), nullable=True),
    sa.Column('last_name', sa.String(length=30), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('company_purchases',
    sa.Column('purchase_id', sa.Integer(), nullable=False),
    sa.Column('item', sa.Text(), nullable=True),
    sa.Column('company_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['company_id'], ['company.company_id'], ),
    sa.PrimaryKeyConstraint('purchase_id')
    )
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column(u'company_contact', sa.Column('contact_name', sa.String(length=255), nullable=True))
    op.create_foreign_key(None, 'company_contact', 'company', ['company_id'], ['company_id'])
    op.create_foreign_key(None, 'contracts', 'company', ['company_id'], ['company_id'])
    op.drop_column(u'contracts', 'contact_name')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'contracts', sa.Column('contact_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'contracts', type_='foreignkey')
    op.drop_constraint(None, 'company_contact', type_='foreignkey')
    op.drop_column(u'company_contact', 'contact_name')
    op.drop_table('roles')
    op.drop_table('company_purchases')
    op.drop_table('users')
    ### end Alembic commands ###