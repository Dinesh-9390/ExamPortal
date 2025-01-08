import uuid
from app import db
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from app.models.audit_columns import AuditColumns


class SubSections(db.Model, AuditColumns):
    __tablename__ = 'sub_sections'

    id = db.Column(UNIQUEIDENTIFIER, primary_key=True, nullable=False, default=uuid.uuid4)
    section_name = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return({
            'id': str(self.id),
            'section_name': self.section_name
        })