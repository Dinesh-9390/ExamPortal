import uuid
from app import db
from app.models.audit_columns import AuditColumns
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy import ForeignKey

class UserTechnology(db.Model, AuditColumns):
    __tablename__ = 'user_technology'

    id = db.Column((PG_UUID(as_uuid=True)),primary_key=True, nullable=False, default=uuid.uuid4)
    user_id = db.Column(ForeignKey('user_mst.id'), nullable=False)
    technology_id = db.Column(ForeignKey('technology_mst.id'), nullable=False)

    def to_dict(self):
        return{
            'id': str(self.id),
            'user_id': str(self.user_id),
            'technology_id': str(self.technology_id)
        }