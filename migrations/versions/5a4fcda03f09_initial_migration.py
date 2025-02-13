"""Initial Migration

Revision ID: 5a4fcda03f09
Revises: 
Create Date: 2025-01-08 09:51:51.271848

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = '5a4fcda03f09'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_mst',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('first_name', sa.String(length=225), nullable=False),
    sa.Column('last_name', sa.String(length=225), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('mobile_number', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_tstmp', sa.DateTime(), nullable=True),
    sa.Column('updated_tstmp', sa.DateTime(), nullable=True),
    sa.Column('created_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('updated_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user_mst.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('mobile_number')
    )
    op.create_table('exams',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('title', sa.String(length=225), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('access_code', sa.String(length=50), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('total_marks', sa.Integer(), nullable=False),
    sa.Column('created_tstmp', sa.DateTime(), nullable=True),
    sa.Column('updated_tstmp', sa.DateTime(), nullable=True),
    sa.Column('created_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('updated_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user_mst.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role_mst',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('role_type', sa.String(length=225), nullable=False),
    sa.Column('created_tstmp', sa.DateTime(), nullable=True),
    sa.Column('updated_tstmp', sa.DateTime(), nullable=True),
    sa.Column('created_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('updated_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user_mst.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('role_type')
    )
    op.create_table('sub_sections',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('section_name', sa.String(length=255), nullable=False),
    sa.Column('created_tstmp', sa.DateTime(), nullable=True),
    sa.Column('updated_tstmp', sa.DateTime(), nullable=True),
    sa.Column('created_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('updated_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user_mst.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('technology_mst',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('technology_name', sa.String(length=225), nullable=False),
    sa.Column('created_tstmp', sa.DateTime(), nullable=True),
    sa.Column('updated_tstmp', sa.DateTime(), nullable=True),
    sa.Column('created_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('updated_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user_mst.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('technology_name')
    )
    op.create_table('user_details',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('user_id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('aadhaar_number', sa.String(), nullable=False),
    sa.Column('college_name', sa.String(length=225), nullable=False),
    sa.Column('roll_number', sa.String(length=50), nullable=False),
    sa.Column('qualification', sa.String(length=255), nullable=True),
    sa.Column('experience_type', sa.String(length=50), nullable=False),
    sa.Column('experience', sa.DECIMAL(), nullable=True),
    sa.Column('created_tstmp', sa.DateTime(), nullable=True),
    sa.Column('updated_tstmp', sa.DateTime(), nullable=True),
    sa.Column('created_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('updated_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_mst.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sections',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('section_name', sa.String(length=255), nullable=False),
    sa.Column('sub_section_id', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('created_tstmp', sa.DateTime(), nullable=True),
    sa.Column('updated_tstmp', sa.DateTime(), nullable=True),
    sa.Column('created_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('updated_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['sub_section_id'], ['sub_sections.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user_mst.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_role_map',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('user_id', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('role_id', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('created_tstmp', sa.DateTime(), nullable=True),
    sa.Column('updated_tstmp', sa.DateTime(), nullable=True),
    sa.Column('created_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('updated_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['role_mst.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_mst.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_technology',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('user_id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('technology_id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('created_tstmp', sa.DateTime(), nullable=True),
    sa.Column('updated_tstmp', sa.DateTime(), nullable=True),
    sa.Column('created_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('updated_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['technology_id'], ['technology_mst.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_mst.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('exam_section',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('exam_id', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('section_id', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('sub_section_id', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('marks', sa.Integer(), nullable=False),
    sa.Column('created_tstmp', sa.DateTime(), nullable=True),
    sa.Column('updated_tstmp', sa.DateTime(), nullable=True),
    sa.Column('created_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('updated_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['exam_id'], ['exams.id'], ),
    sa.ForeignKeyConstraint(['section_id'], ['sections.id'], ),
    sa.ForeignKeyConstraint(['sub_section_id'], ['sub_sections.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user_mst.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questions_mst',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('question_type', sa.String(length=50), nullable=False),
    sa.Column('section_id', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('sub_section_id', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('question', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('positive_weightage', sa.String(length=50), nullable=True),
    sa.Column('negative_weightage', sa.String(length=50), nullable=True),
    sa.Column('created_tstmp', sa.DateTime(), nullable=True),
    sa.Column('updated_tstmp', sa.DateTime(), nullable=True),
    sa.Column('created_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('updated_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['section_id'], ['sections.id'], ),
    sa.ForeignKeyConstraint(['sub_section_id'], ['sub_sections.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user_mst.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_exam_map',
    sa.Column('id', mssql.UNIQUEIDENTIFIER(), nullable=False),
    sa.Column('user_id', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('exam_id', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('current_question_id', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('start_time', sa.DATETIME(), nullable=False),
    sa.Column('end_time', sa.DATETIME(), nullable=False),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('created_tstmp', sa.DateTime(), nullable=True),
    sa.Column('updated_tstmp', sa.DateTime(), nullable=True),
    sa.Column('created_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('updated_by', mssql.UNIQUEIDENTIFIER(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['current_question_id'], ['questions_mst.id'], ),
    sa.ForeignKeyConstraint(['exam_id'], ['exams.id'], ),
    sa.ForeignKeyConstraint(['updated_by'], ['user_mst.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user_mst.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_exam_map')
    op.drop_table('questions_mst')
    op.drop_table('exam_section')
    op.drop_table('user_technology')
    op.drop_table('user_role_map')
    op.drop_table('sections')
    op.drop_table('user_details')
    op.drop_table('technology_mst')
    op.drop_table('sub_sections')
    op.drop_table('role_mst')
    op.drop_table('exams')
    op.drop_table('user_mst')
    # ### end Alembic commands ###
