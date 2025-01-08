import uuid
from app import db
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from app.models.audit_columns import AuditColumns
from sqlalchemy import ForeignKey


class Sections(db.Model, AuditColumns):
    __tablename__ = 'sections'

    id = db.Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False, default=uuid.uuid4)
    section_name = db.Column(db.String(255), nullable=False)
    sub_section_id = db.Column(ForeignKey('sub_sections.id'))

    def to_dict(self):
        return({
            'id': str(self.id),
            'section_name': self.section_name,
            'sub_section_id': str(self.sub_section_id)
        })