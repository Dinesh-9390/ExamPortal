import uuid
from app import db
from sqlalchemy.dialects.mssql import UNIQUEIDENTIFIER
from app.models.audit_columns import AuditColumns

class RoleMst(db.Model, AuditColumns):
    __tablename__ = 'role_mst'

    id = db.Column(UNIQUEIDENTIFIER, primary_key=True,  nullable=False, default=uuid.uuid4)
    role_type = db.Column(db.String(225), unique=True, nullable=False)

    def to_dict(self):
        return {
        'id': str(self.id),
        'role_type': self.role_type
        }