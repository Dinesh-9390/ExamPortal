import uuid
from app import db
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from app.models.audit_columns import AuditColumns


class SubSections(db.Model, AuditColumns):
    __tablename__ = 'sub_sections'

    id = db.Column(PG_UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4)
    section_name = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return({
            'id': str(self.id),
            'section_name': self.section_name
        })