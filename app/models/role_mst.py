import uuid
from app import db
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from app.models.audit_columns import AuditColumns

class RoleMst(db.Model, AuditColumns):
    __tablename__ = 'role_mst'

    id = db.Column(PG_UUID(as_uuid=True), primary_key=True,  nullable=False, default=uuid.uuid4)
    role_type = db.Column(db.String(225), unique=False, nullable=False)

    def to_dict(self):
        return {
        'id': str(self.id),
        'role_type': self.role_type
        }